# Dictionary example
aPerson = {
    "Name":"Saeed",
    "Age":47,
    "Job":"Business Analyst",
    "City":"Calgary"}
aPerson["Name"]="Omar"
print(aPerson["Name"])
aPerson
aPerson["Name"]="Saeed"

# Loop example game
myList = [1,2,3,4,7,8]
n = "yes"

while n == "yes":
    x = int(input("Please enter a number: "))
    if x in myList:
        print("YES... in the list.")
    else:
        print("Sorry! Not in the list.")
    n = input("Do you want to play again? ")

print("Thank you for playing!")