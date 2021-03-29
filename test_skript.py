import json

lists_description = []
with open("my_json_file.json") as json_file_description:
    date = json.load(json_file_description)
    for date1 in date:
        lists_description.append(date1["description"])

print(lists_description[2])
