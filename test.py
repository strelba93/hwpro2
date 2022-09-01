import re
list = [['oleg', '', '16 years'],['oleg', 'pidor', '']]

# for items in list:
#     for i, n in enumerate(list):
#         if n == ''




list_1 = [item for sublist in zip(list[0], list[1]) for item in sublist]

# for a, b in zip(list[0], list[1]):

print(list_1)