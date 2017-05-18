#coding=utf8
from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Post, Permission
from . import api
from .decorators import permission_required
from .errors import forbidden

#获取文章集合
@api.route('/posts/')
def get_posts():
    page = request.args.get('page', 1, type=int)
    '''
    分页
    Flask-SQLAlchemy提供的paginate()方法： 页数是paginate()方法的第一个参数，也是唯一必需的参数。可选参数per_page用来指定每页显示的记录数量;如果没有
    指定，则默认显示20个记录。另一个可选参数为error_out，当其设为True时(默认值)，如果请求的页数超出了范围，则会返回404错误;如果设为False，页数超出范
    围时会返回一个空列表
    '''
    pagination = Post.query.paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)  # paginate()方法的返回值是一个Pagination类对象（分页对象）
    posts = pagination.items  #items：当前页面中的记录
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page+1, _external=True)
    return jsonify({
        'posts': [post.to_json() for post in posts],  #文章集合（完整集合的一部分）
        'prev': prev,   #如果资源有上一页和下一页，prev和next字段分别表示上一页和下一页资源的URL
        'next': next,
        'count': pagination.total  #集合中博客文章的总数
    })


#返回单篇博客文章
@api.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())


#文章资源POST请求的处理程序: 把一篇新博客文章插入数据库
@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE_ARTICLES)  #权限检查: 确保通过认证的用户有写博客文章的权限
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    '''
    响应的主体中包含了新建的资源。如此一来客户端就无需在创建资源后再立即发起一个GET请求以获取资源
    写入数据库之后会返回201状态码，并把Location首部的值设为刚创建的这个资源的URL
    '''
    return jsonify(post.to_json()), 201, \
        {'Location': url_for('api.get_post', id=post.id, _external=True)}

#文章资源PUT请求的处理程序: 更新现有资源
@api.route('/posts/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE_ARTICLES) #权限检查: 确保通过认证的用户有写博客文章的权限
def edit_post(id):
    post = Post.query.get_or_404(id)
    if g.current_user != post.author and \
            not g.current_user.can(Permission.ADMINISTER):   #权限检查: 保证用户是文章的作者或者是管理员
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    return jsonify(post.to_json())
