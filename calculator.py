import os

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b


def divie(a,b):
    return a/b








from art import logo

print(logo)
end_of_calc=False
first_time=True
while end_of_calc==False:
    if first_time == True:
        first_nr=int(input("What's the first number?: "))
    action=input("\n+\n-\n*\n/\nPick an operation: ")
    next_number=int(input("What's the second number?: "))

    if action=='+':
        print(f"{first_nr} {action} {next_number} = {(add(a=first_nr,b=next_number))}")
        first_nr=add(a=first_nr,b=next_number)
    elif action=='-':
        print(f"{first_nr} {action} {next_number} = {(substract(a=first_nr, b=next_number))}")
        first_nr=substract(a=first_nr, b=next_number)
    elif action=='*':
        print(f"{first_nr} {action} {next_number} = {multiply(a=first_nr, b=next_number)}")
        first_nr=multiply(a=first_nr, b=next_number)
    elif action=="/":
        print(f"{first_nr} {action} {next_number} = {divie(a=first_nr, b=next_number)}")
        first_nr=divie(a=first_nr, b=next_number)
    else:
        print("Invalid action was chosen")

    next_operation=input(f"Type 'y' to continue calculating with {first_nr} or type 'n' to start a new calculation: " ).lower()
    if next_operation=='y':
        first_time=False
    elif next_operation=='n':
        end_question=input("If you wanna terminate Calculator aplication type 'y'.: ").lower()
        if end_question=='y':
            end_of_calc=True
        else:
            clear = lambda: os.system('cls')
            clear()
    else:
        print("Invalid answer")
        end_question = input("If you wanna terminate Calculator aplication type 'y'.: ").lower()
        if end_question == 'y':
            end_of_calc = True



