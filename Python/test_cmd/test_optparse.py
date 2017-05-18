#coding=utf8
from optparse import OptionParser
'''
optparse太老已废弃，被argparse取代
'''

parser = OptionParser()


parser.add_option("-n", type="int", dest='num')

'''
type
保证类型的正确性，默认是'string'类型

dest
变量名，解析的值会存储在该变量中，如果没有指定dest参数，将用命令行的参数名来对options对象的值进行存取（如：-n就存到变量n中）
'''

parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")

'''
help
指定帮助信息文本，当optparse解析到-h或者–help命令行参数时，会调用parser.print_help()打印程序的帮助信息，打印出帮助信息后，optparse将会退出，不再解析其它的命令行参数


'''


parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
'''
action
指示optparse当解析到一个命令行参数时该如何处理。actions有一组固定的值可供选择，(没有action参数)默认是store表示将命令行参数值保存在options对象里
store_true和store_false ，用于处理带命令行参数后面不带值的情况，如：
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose")
这样的话，当解析到 ‘-v’，options.verbose将被赋予True值，反之，解析到 ‘-q’，会被赋予False值

其它的actions值还有：store_const 、append 、count 、callback

'''


parser.add_option("-p", "--pdbk", action="store_true",
                  dest="pdcl",
                  default=False,
                  help="write pdbk data to oracle db")

parser.add_option("-z", "--zdbk", action="store_true",
                  dest="zdcl",
                  default=False,
                  help="write zdbk data to oracle db")


(options, args) = parser.parse_args()  #也可以传递一个命令行参数列表到parse_args()；否则，默认使用 sys.argv[:1]
#options，它是一个对象（optpars.Values），保存有命令行参数值。只要知道命令行参数名dest，如filename，就可以访问其对应的值： options.filename
#args，它是一个由位置参数组成的列表


print 'options: ', options
print 'args', args
