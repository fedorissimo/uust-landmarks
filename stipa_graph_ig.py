import csv
import matplotlib.pyplot as plt

howmuch, number_of_students = [], []

with open('stipa.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for i in reader:
        howmuch.append(i[0])
        number_of_students.append(int(i[1]))

plt.bar(howmuch, number_of_students)
plt.ylabel('Количество студентов')
plt.xlabel('Размер стипендии')
plt.show()