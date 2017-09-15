#coding=utf8
import jpype
import os.path

#jvm.dll path
jvmpath = jpype.getDefaultJVMPath()

print(jvmpath)

jpype.startJVM(jvmpath)

jpype.java.lang.System.out.println("hello World")

jpype.shutdownJVM()
