'''
Problem Set I - Regex

Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).


{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},
{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): 
Parameter must be an array or an object that implements Countable (153)"}]}

'''
import re
import json

data = {
    "orders":[
        {"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},
        {"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},
        {"id":650},{"id":651},{"id":652},{"id":653}
        ],
        "errors":[
            {"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}
            ]
        }


text = json.dumps(data)

pattern = r'"id":\s*(\d+)|"code":\s*(\d+)'


matches = re.findall(pattern, text)

result = [int(num) for match in matches for num in match if num]

print(result)
