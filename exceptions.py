notNum=True
while notNum:
    try:
        x = input("Please enter a whole number")

        x = int(x)
        notNum = False
    except ValueError:
        print("Asa-dude? I asked for a integer not a ",x)
print("your number was",x)