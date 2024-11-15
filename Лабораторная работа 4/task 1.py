import json
# TODO решите задачу
def task() -> float:
    file = open("input.json")
    data = json.load(file)
    result = 0
    for i in data:
        result += i["score"]*i["weight"]
    return round(result,3)
print(task())
