#!/usr/bin/python3
import json

a = {'name': 'max',
     'age': 22,
     'marks': [43, 32, 43, 90],
     'pass': True
     }

# print(json.dumps(a))
with open("demo.json", "w")as f:
    f.write(json.dumps(a, indent=4))
