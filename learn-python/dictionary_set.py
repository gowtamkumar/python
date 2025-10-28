info = {
    "name": "Gowtam kumar",
    "age": 21,
    "city": "Jashore",
    "skills": ["Python", "Django", "JavaScript"],
}
print(info.keys())
print(info.values())
# convert values to a list
values_list = list(info.values())
print(values_list)
# convert to tuple
print(info.items())
print(list(info.items()))

print(info["name"])
print(info.get("name"))  # this good

new_info = {"is_student": False, "is_employed": True}
info.update(new_info)
print(info)
