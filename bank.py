x = input('Enter your pin:')
"""""
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
"""
print('Hello, ' + x)
print("1.balenced amount in bank\n 2.withdraw\n 3.deposit\n")
m = int(input("enter the choice:"))
total = 1000
if m==1:
    if withdraw ==0:
     balenced_amount = total - withdraw
    print("balenced amount is:",balenced_amount)

if m==2:
    withdraw = int(input("enter the withdraw:"))
    print("withdraw amount is:",withdraw)
if m == 3:
        print("deposit:", 456)
"""""
def number_to_string(agrument):
    switcher = {
        0: input('enter the amount:'),
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    argument=0
    print (number_to_string(argument))
"""