----- HTMLTestRunner的几个BUG -----

1.显示出界的问题
打开HTMLTestRunner.py  , 找到如下代码部分（312行，见红色部分）：
 STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         {  }            /*  312行   */
在pre 的{ }中添加： word-wrap:break-word;word-break:break-all;overflow:auto; 即：
pre         {  word-wrap:break-word;word-break:break-all;overflow:auto;}

这种办法容易使日志log显示的不全，但是可以通过向后移动查看全部。好像也不是很人性化

2.扩大背后的区域放大，让它看起来没有出界
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    /*width: 500px; */       注释掉或者删除本行
}

3.log显示中文乱码的问题
在执行所有case的程序中添加如下代码：
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
