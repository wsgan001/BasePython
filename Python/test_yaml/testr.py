#coding=utf8
import yaml

with open('tree.yaml') as f:
    dataMap = yaml.load(f)
    print dataMap
