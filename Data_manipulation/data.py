persons = [
    {"name": "kunj", "age": 30, "city": "ujjain"},
    {"name": "rk", "age": 22, "city": "indore"},
    {"name": "chirag", "age": 25, "city": "ratlam"}
]
filtered_persons = []
for person in persons:
    if person["age"] >= 25:
        filtered_persons.append(person)
sorted_persons = sorted(filtered_persons)

for person in sorted_persons:
    print("Name:", person["name"], "| Age:", person["age"], "| City:", person["city"])
