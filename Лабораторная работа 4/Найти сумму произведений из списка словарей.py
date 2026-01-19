# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r") as f:
        return round(sum(i["score"] * i["weight"] for i in json.load(f)), 3)

print(task())

