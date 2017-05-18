#coding=utf8
from flask import render_template, request, jsonify
from . import main


@main.app_errorhandler(403)  #在错误处理程序中根据客户端请求的格式改写响应，这种技术称为内容协商
def forbidden(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:  #检查Accept请求首部(Werkzeug 将其解码为 request.accept_ mimetypes)，根据首部的值决定客户端期望接收的响应格式
        response = jsonify({'error': 'forbidden'})   #从Python字典中生成json
        response.status_code = 403
        return response
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500
