from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)



for items in contacts_list:
  b = items[0].split(" ")
  c = items[1].split(" ")
  if len(b) == 3:
    items[0] = b[0]
    items[1] = b[1]
    items[2] = b[2]
  if len(b) == 2:
    items[0] = b[0]
    items[1] = b[1]
  if len(c) == 2:
    items[1] = c[0]
    items[2] = c[1]

for items in contacts_list:
  for i, n in enumerate(items):
    pat_1 = re.compile('(\+?)(7|8)(\ ?)(\(?)(\d{3})(\)?)(\-?)(\ ?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})')
    res_1 = re.sub(pat_1, r'+7(\5)\9-\11-\13', n)
    items[i] = res_1

for items in contacts_list:
  for i, n in enumerate(items):
    pat_2 = r'(\ )?(\,)?(\()?(доб.)(\ )?(\d*)(\))?'
    if 'доб' in n:
      res_2 = re.sub(pat_2, r'доб.\6', n)
      print(res_2)
      items[i] = res_2







with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)