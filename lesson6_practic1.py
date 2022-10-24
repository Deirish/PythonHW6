# Создать словарь оценок предполагаемых студентов
# (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.
students = {"Ivanov_Ivan": [12, 10, 8, 7, 9, 5], "Smirnov_Nikolay": [10, 6,
                                                                     5, 8, 7, 3],
            "Petrov_Alexandr": [11, 9, 5, 7, 4, 8], "Sidorov_Alexey": [12, 8, 4, 5, 7, 3],
            "Vasilenko_Marina": [10, 8, 7, 5, 9, 8], "Denisenko_Inna": [9, 6, 8, 7, 9, 10]}
def val(lst):
    return sum(lst) // len(lst)
points = sorted(students.keys(), key = lambda studentid: val(students[studentid]))
print("Luchshyi", points[-1] )
print("Hudshyi", points[0])

# points = {values: sum(map(lambda i: int(i[0]), students[values])) for values in students}
# print(points)

# points = sum(students.values[1])
# print(points)
# for poins in students:




# print(students.values())
# average = sum(students.values()) // 6
# print(average)