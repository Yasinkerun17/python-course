grade = int(input("enter your grade between 0 - 100 : "))

if 90 <= grade < 100:
    print("Grade A")
elif 80 <= grade < 90:
    print("Grade B")
elif 70 <= grade < 80:
    print("Grade c")
elif 60 <= grade < 70:
    print("Grade D")
elif 0 <= grade < 60:
    print("Grade F")
else:
    print("enter value between 0 and 100")
