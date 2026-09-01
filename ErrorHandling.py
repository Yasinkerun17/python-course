
# def Type_Error():
#     try:
#         for i in ['a','b','c']:
#             print(i**2)
#     except TypeError:
#         print("type error here")
    
# Type_Error()

# def Zero_Division_error():
#     try:
#         x = 5
#         y = 5
#         print(x/y)
#     except ZeroDivisionError:
#         print("Zero Division Error \n denominator cannot be zero")
#     finally:
#         print("All Done")

# Zero_Division_error()

def ask():
    while True:
        try:
            number = int(input("Enter a Number: "))
        except ValueError:
            print("An Error occurred! Please try again!")
            continue
        else:
            print(f"Thank You your number squared is {number * number}")
            break

ask()