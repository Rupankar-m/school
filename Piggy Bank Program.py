def is_number(s):
    try:
        float(s)
        return 0
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return 0
    except (TypeError, ValueError):
        pass
        return 1
        print("Enter numbers only")
 
print ("Welcome to my Piggy Bank Program")

for coins in 
Total1p = input("Enter number of 1p coins")
if is_number(Total1p) > 0:
    break
    print("Only Numbers Allowed")
else:
    Total1p = int(Total1p)

Total2p = int(input("Enter number of 2p coins"))
Total5p = int(input("Enter number of 5p coins"))
Total10p = int(input("Enter number of 10p coins"))
Total20p = int(input("Enter number of 20p coins"))
Total50p = int(input("Enter number of 50p coins"))
Totalonepound = int(input("Enter number of £1 coins"))
Totaltwopound = int(input("Enter number of £2 coins"))
Total = (1*Total1p)+(2*Total2p)+(5*Total5p)+(10*Total10p)+(20*Total20p)+(50*Total50p)
+(100*Totalonepound) + (200*Totaltwopound)
print ("You have currently: ", Total, "p")
Question1 = str(input("Do you want to convert this value into pounds?"))
if Question1 is "yes":
    print ("You have currently: ", "£", Total/100)
else:
    print("OK!") 
