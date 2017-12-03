Total1p = input("Enter number of 1p coins? ")
while type(Total1p) != int:
    try:
        Total1p = int(Total1p)
    except ValueError:
        Total1p = input("Invalid input, please try again. Enter number of 1p coins? ")

Total2p = input("Enter number of 2p coins? ")
while type(Total2p) != int:
    try:
        Total2p = int(Total2p)
    except ValueError:
        Total2p = input("Invalid input, please try again. Enter number of 2p coins? ")

Total5p = input("Enter number of 5p coins? ")
while type(Total5p) != int:
    try:
        Total5p = int(Total5p)
    except ValueError:
        Total5p = input("Invalid input, please try again. Enter number of 5p coins? ")

Total10p = input("Enter number of 10p coins? ")
while type(Total10p) != int:
    try:
        Total10p = int(Total10p)
    except ValueError:
        Total10p = input("Invalid input, please try again. Enter number of 10p coins? ")

Total20p = input("Enter number of 20p coins? ")
while type(Total20p) != int:
    try:
        Total20p = int(Total20p)
    except ValueError:
        Total20p = input("Invalid input, please try again. Enter number of 20p coins? ")

Total50p = input("Enter number of 50p coins? ")
while type(Total50p) != int:
    try:
        Total50p = int(Total50p)
    except ValueError:
        Total50p = input("Invalid input, please try again. Enter number of 50p coins? ")

Totalonepound = input("Enter number of £1 coins? ")
while type(Totalonepound) != int:
    try:
        Totalonepound = int(Totalonepound)
    except ValueError:
        Totalonepound = input("Invalid input, please try again. Enter number of £1 coins? ")

Totaltwopound = input("Enter number of £2 coins? ")
while type(Totaltwopound) != int:
    try:
        Totaltwopound = int(Totaltwopound)
    except ValueError:
        Totaltwopound = input("Invalid input, please try again. Enter number of £2 coins? ")



Total = (1*Total1p)+(2*Total2p)+(5*Total5p)+(10*Total10p)+(20*Total20p)+(50*Total50p)
+(100*Totalonepound) + (200*Totaltwopound)
print ("You have currently: ", Total, "p")
Question1 = str(input("Do you want to convert this value into pounds? "))
if Question1.lower() == "yes":
    print ("You have currently: ", "£", Total/100)
else:
    print("OK!")
