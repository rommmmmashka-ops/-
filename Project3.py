students = {}
name = ""

Astudents = {}
Bstudents = {}
Cstudents = {}
Dstudents = {}

while True:
    name = input("ведіть ім'я студента:")
    if name.lower() == "stop":
        break
    mark = int(input("Введіть оцінку студента:"))
    if name and mark:
        students[name] = mark

print("Cтуденти та їх оцінки:", ", ".join([f"{name} – {mark}" for name, mark in students.items()]))

if students:
    print("Середній бал групи:",sum(students.values())/len(students))

for i in students:
    mark = students.get(i)
    if mark >= 10:
        Astudents[i] = mark
    elif mark >= 7:
        Bstudents[i] = mark
    elif mark >= 4:
        Cstudents[i] = mark
    else:
        Dstudents[i] = mark

print("Відмінники:", len(Astudents), ", ".join(Astudents))
print("Хорошисти:", len(Bstudents), ", ".join(Bstudents))
print("Відстаючі:", len(Cstudents), ", ".join(Cstudents))
print("Не здали:", len(Dstudents), ", ".join(Dstudents))


