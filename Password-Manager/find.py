import json
with open("data.json", "r") as file_data:
    data = json.load(file_data)
for key, value in data.items():
    for x in value:
        y = [value for value in value.items()]



# x = {key: f"\n{value}" for (key, value) in data.items()}
# y = [value for value in data]
print(y[0][1], y[1][1])
