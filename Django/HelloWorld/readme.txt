
1、项目目录结构说明
|-- HelloWorld
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py

HelloWorld: 项目的容器
manage.py: 一个实用的命令行工具，可让你以各种方式与该Django项目进行交互
HelloWorld/__init__.py: 一个空文件，告诉Python该目录是一个Python包
HelloWorld/settings.py: 该Django项目的设置/配置
HelloWorld/urls.py: 该Django项目的URL声明; 一份由Django驱动的网站"目录"
HelloWorld/wsgi.py: 一个WSGI兼容的Web服务器的入口，以便运行你的项目


2、Django模板标签
1）if/else标签
基本语法格式如下：
{% if condition %}
     ... display
{% endif %}
或者：
{% if condition1 %}
   ... display 1
{% elif condiiton2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}

{% if %}标签接受and，or或者not关键字来对多个变量做判断，或者对变量取反（not)，例如：
{% if athlete_list and coach_list %}
     athletes和coaches变量都是可用的
{% endif %}

2）for标签
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}

增加一个reversed使得该列表被反向迭代：
{% for athlete in athlete_list reversed %}
...
{% endfor %}

嵌套使用：
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}


3）ifequal/ifnotequal 标签
比较两个值，当他们相等时显示在{% ifequal %}和{% endifequal %}之中所有的值
{% ifequal user currentuser %}
    <h1>Welcome!</h1>
{% endifequal %}

{% else %}标签可选：
{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}


4）注释标签
{# 这是一个注释 #}


5）过滤器
模板过滤器可以在变量被显示前修改它，过滤器使用管道字符
{{ name|lower }}
{{ my_list|first|upper }}
{{ bio|truncatewords:"30" }}    #过滤器的参数跟随冒号之后并且总是以双引号包含  显示变量bio的前30个词

addslashes: 添加反斜杠到任何反斜杠、单引号或者双引号前面
date : 按指定的格式字符串参数格式化 date 或者 datetime 对象，实例：{{ pub_date|date:"F j, Y" }}
length : 返回变量的长度

6）include标签
{% include %}标签允许在模板中包含其它的模板的内容




