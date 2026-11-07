import csv
import matplotlib.pyplot as plt

places, types = [], []

with open('places_by_type.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    c = 0
    for i in reader:
        if c == 0:
            c = 1
            continue
        places.append(i[0])
        types.append(i[1])

dif_types = list(set(types))
print(dif_types)
numbers_of_cafes = [types.count(i) for i in dif_types]
plt.pie(numbers_of_cafes, labels=dif_types)
plt.show()
