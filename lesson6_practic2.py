# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd,
# FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

Python = {1: "Ivanov_Ivan", 2: "Smirnov_Nikolay", 3: "Petrov_Alexandr",
          3: "Sidorov_Alexey", 4: "Vasilenko_Marina", 5: "Denisenko_Inna", \
           6: "Rudenko_Vitaliy", 7: "Osadchaya_Irina"}

FrontEnd = {1: "Petrov_Alexandr", 2: "Agafonov_Mihail", 3: "Chuprin_Evgeniy",
            4: "Shabanova_Taisiya", 5: "Stadnik_Alyona", 6: "Denisenko_Inna",
            7: "Klimov_Vladislav"}

FullStack = {1: "Chuprin_Evgeniy", 2: "Klimov_Vladislav",
             3: "Krivenko_Vladislava", 4: "Shevchenko_Darina",
             5: "Linnik_Elena", 6: "Voloshin_Maxim", 7: "Kupin_Sergey"}

Java = {1: "Teslenko_Marina", 2: "Lukinov_Roman", 3: "Solyanik_Andrey",
        4: "Gromov_Klim", 5: "Osadchaya_Irina", 6: "Ponkratov_Denis",
        7: "Deineko_Nazar"}

for students in Python, FrontEnd, FullStack, Java:
        if students == Python or students == Java:
            print(students.values())
            if students != FrontEnd:
             print(students.values())
            elif students.values() > 2:
                print(students.values())








# students = [["Python", "Ivanov_Ivan", "Smirnov_Nikolay", "Petrov_Alexandr",
#       "Sidorov_Alexey", "Vasilenko_Marina", "Denisenko_Inna",
#       "Rudenko_Vitaliy", "Osadchaya_Irina"], ["FrontEnd", "Petrov_Alexandr",
#       "Agafonov_Mihail", "Chuprin_Evgeniy", "Shabanova_Taisiya",
#       "Stadnik_Alyona", "Denisenko_Inna", "Klimov_Vladislav"], ["Java",
#       "Teslenko_Marina", "Lukinov_Roman", "Solyanik_Andrey", "Gromov_Klim",
#       "Osadchaya_Irina", "Ponkratov_Denis", "Deineko_Nazar"], ["FuulStack",
#       "Chuprin_Evgeniy", "Klimov_Vladislav", "Krivenko_Vladislava",
#       "Shevchenko_Darina", "Linnik_Elena", "Voloshin_Maxim"]]
#
# new_l = {x[0]: x[1:] for x in students}
# print(new_l)
#




