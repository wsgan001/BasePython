#coding=utf8


'''
os.path.commonprefix(list) #返回list(多个路径)中，所有path共有的最长的路径。

os.path.lexists  #路径存在则返回True,路径损坏也返回True

os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录

os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”

os.path.getatime(path)  #返回最后一次进入此path的时间。

os.path.getmtime(path)  #返回在此path下最后一次修改的时间。

os.path.getctime(path)  #返回path的大小

os.path.isabs(path)  #判断是否为绝对路径

os.path.islink(path)  #判断路径是否为链接

os.path.ismount(path)  #判断路径是否为挂载点（）

os.path.normcase(path)  #转换path的大小写和斜杠

os.path.normpath(path)  #规范path字符串形式

os.path.realpath(path)  #返回path的真实路径

os.path.relpath(path[, start])  #从start开始计算相对路径

os.path.samefile(path1, path2)  #判断目录或文件是否相同

os.path.sameopenfile(fp1, fp2)  #判断fp1和fp2是否指向同一文件

os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件

os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组

os.path.splitunc(path)  #把路径分割为加载点与文件

os.path.supports_unicode_filenames  #设置是否支持unicode路径名
'''
