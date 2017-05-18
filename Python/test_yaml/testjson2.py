#coding=utf8
import json,yaml

str = '{ "foo": "bar" }'
data = json.loads(str)
yml = yaml.safe_dump(data)

print yml
