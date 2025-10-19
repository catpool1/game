import json
with open('rooms/test.json', 'r') as f:
    js = json.load(f)

print(js['player'])