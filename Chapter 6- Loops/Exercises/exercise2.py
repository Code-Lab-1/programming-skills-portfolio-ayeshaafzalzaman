while True:
    age=int(input("your age is=="))
    if age=='quit':
        break
    if age< 3:
        print("you get in free!")
    elif age< 13:
        print("your ticket is $10.")
    else:
        print("your ticket is $15")
        break