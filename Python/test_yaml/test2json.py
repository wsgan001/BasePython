#coding=utf8
import yaml,json

yml = """

---

  foo: bar

"""

data = yaml.load(yml)
json = json.dumps(data)
print json
