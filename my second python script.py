age = int(input("How old are you?:"))

if age >= 21:
    print("Access Granted with drinks!")
elif age >= 18:
    print('Access Granted but no drinks!')
else:
    print("Go home kid!")