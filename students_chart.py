import csv
import matplotlib.pyplot as plt

buildings, number_of_students = [], []

with open('students_by_building.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    c = 0
    for i in reader:
        if c == 0:
            c = 1
            continue
        buildings.append(i[0])
        number_of_students.append(int(i[2]))

plt.pie(number_of_students, labels=buildings)
plt.show()