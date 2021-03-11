# Loop example

myFamily = [
    {
         "Name":"Saeed",
         "Age":47,
         "Job":"Business Analyst",
         "City":"Calgary"
         },
    {
         "Name":"Joudi",
         "Age":41,
         "Job":"Banker",
         "City":"Calgary"
         },
    {
         "Name":"Salma",
         "Age":14,
         "Job":"Student",
         "City":"Calgary"
         }
    ]

'''
i = 0
for items in aPerson.items():
    print(items)

for anyName, anyName2 in aPerson.items():
    print(anyName, " : ",anyName2)
'''
for member in myFamily:
     print(member["Age"])