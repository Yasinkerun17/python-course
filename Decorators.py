# def hello(greet):
#     print("Hello")
#     def welcome():
#         return greet()

#     return welcome

# def new_func():
#      return "Hi new function \n"

# some_func = hello(new_func)

# print(some_func())

def hello(greet):
    def welcome():
        print("Hello")
        return greet()

    return welcome

@hello
def new_func():
     return "Hi new function \n"

print(new_func())