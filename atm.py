#ATM Program
print("Welcome to State bank of India")

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
print("1.withdraw\n 2.balenced amount in bank\n  3.deposit\n")
m = int(input("enter the choice:"))
t = 1000
if m==1:
    w = int(input("Enter withdraw amount: "))
    if (w <= t and w % 100 == 0):
        print("Please take your amount:", w)
    else:
        print("Invalid cash")

elif(m==2):
 print("Your available amount : ",t)
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