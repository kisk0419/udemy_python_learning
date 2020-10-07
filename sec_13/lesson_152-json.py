"""
Json
"""
import json

d = {
    "employee": [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

print(f'python: {d}')

j = json.dumps(d)
print(f'python->json: {j}')

p = json.loads(j)
print(f'json->python: {p}')

# write python dict to file as json.
with open('lesson_152.json', 'w') as f:
    json.dump(d, f)

# read json from file as python dict.
with open('lesson_152.json', 'r') as f:
    l = json.load(f)
    print(f'json file->python: {l}')