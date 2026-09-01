my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0 
while i < 3:
    for x in my_list:
        if x == "Monday":
            continue
        print(x)
    
    i += 1