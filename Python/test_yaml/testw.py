#coding=utf8
import yaml

dataMap = {'treeroot': {'branch2': {'branch2-1': {'name': 'Node 2-1'}, 'name': 'Node 2'}, 'branch1': {'branch1-1': {'name': 'Node 1-1'}, 'name': 'Node 1'}}}

with open('newtree.yaml', "w") as f:
    yaml.dump(dataMap, f)
