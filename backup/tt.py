import json
from base import file_operation,readConfig

param = {"hhh": "new_value"}
data = file_operation.read_file('test.json')
json_d = json.dumps(data)
print(json_d)
new = json.dumps({**json.loads(json_d), **param})
print(new)