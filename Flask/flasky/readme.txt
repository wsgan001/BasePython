
1、程序的权限
操作                      位值                  说明
----------------------------------------------------------------------------
关注用户                  0b00000001(0x01)      关注其他用户
在他人的文章中发表评论     0b00000010(0x02)      在他人撰写的文章中发布评论
写文章                    0b00000100(0x04)      写原创文章
管理他人发表的评论         0b00001000(0x08)      查处他人发表的不当评论
管理员权限                0b10000000(0x80)      管理网站



2、用户角色
用户角色        权限               说明
----------------------------------------------------------------------------
匿名          0b00000000(0x00)    未登录的用户。在程序中只有阅读权限
用户          0b00000111(0x07)    具有发布文章、发表评论和关注其他用户的权限。这是新用户的默认角色
协管员        0b00001111(0x0f)    增加审查不当评论的权限
管理员        0b11111111(0xff)    具有所有权限，包括修改其他用户所属角色的权限


3、Flask-SQLAlchemy分页对象的属性（paginate()方法的返回值是一个Pagination类对象，这个类在Flask-SQLAlchemy中定义）
属性          说明
-----------------------------------------
items        当前页面中的记录
query        分页的源查询
page         当前页数
prev_num     上一页的页数
next_num     下一页的页数
has_next     如果有下一页，返回True
has_prev     如果有上一页，返回True
pages        查询得到的总页数
per_page     每页显示的记录数量
total        查询返回的记录总数


4、在Flask-SQLAlchemy分页对象上可调用的方法（模板中使用 模板宏文件：_macros.html）
方法             说明
----------------------------------------------------------------------------------
iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2)
一个迭代器，返回一个在分页导航中显示的页数列表。这个列表的最左边显示left_edge页，当前页的左边显示left_current页，当前页的右边显示right_current页，最右边显示right_edge页。例如，在一个100页的列表中，当前页为第50页，使用默认配置，这个方法会返回以下页数:1、2、None、48、49、50、51、52、53、54、55、None、99、100。None表示页数之间的间隔

prev()      上一页的分页对象
next()      下一页的分页对象


5、富文本文章
PageDown: 使用JavaScript实现的客户端Markdown到HTML的转换程序
Flask-PageDown: 为Flask包装的PageDown，把PageDown集成到Flask-WTF表单中
Markdown: 使用Python实现的服务器端Markdown到HTML的转换程序
Bleach: 使用Python实现的HTML清理器

pip install flask-pagedown markdown bleach



6、Werkzeug是Python的WSGI规范的实用函数库。使用广泛，基于BSD协议。

7、Flask-SQLAlchemy记录的查询信息（get_debug_queries()函数返回一个列表，其元素是请求中执行的查询）
名称            说明
----------------------------------------------------------------------------------
statement       SQL语句
parameters      SQL语句使用的参数
start_time      执行查询时的时间
end_time        返回查询结果时的时间
duration        查询持续的时间，单位为秒
context         表示查询在源码中所处位置的字符串





