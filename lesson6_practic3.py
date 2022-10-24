# Написать функцию перевода размеров женского белья из международного во все
# остальные. Внтри функции нужно просто обращаться к правильно составленному
# словарю.

outerwear_dresses_pants = [["Size_S", "Russia_40", "Sweden_34", "France_36",
                            "Italy_38", "UK_8", "USA_6"], ["Size_M", "Russia_42",
                            "Sweden_36", "France_38", "Italy_40", "UK_10", "USA_8"],
                           ["Size_ML", "Russia_44", "Sweden_38", "France_40",
                            "Italy_42", "UK_12", "USA_10"], ["Size_L",
                            "Russia_46", "Sweden_40", "France_42", "Italy_44",
                            "UK_14", "USA_12"], ["Size_LXL", "Russia_48",
                            "Sweden_42", "France_44", "Italy_46", "UK_16",
                            "USA_14"], ["Size_XL", "Russia_50", "Sweden_44",
                            "France_46", "Italy_48", "UK_18", "USA_16"],
                           ["Size_XL-XXL", "Russia_52", "Sweden_46", "France_48",
                            "Italy_50", "UK_20", "USA_18"], ["Size_XXXL",
                            "Russia_54", "Sweden_48", "France_50", "Italy_52",
                            "UK_22", "USA_18"]]

size_chart = {x[0]: x[1:] for x in outerwear_dresses_pants}

my_size = input()
def sizes(my_size):
    return size_chart.get(my_size)
print(size_chart.get(my_size))



