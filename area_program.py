def square(x):
 area_1 = (x**2)
 return area_1
def triangle(x, y):
 area_2 = (0.5 * x * y)
 return area_2

def rectangle(x, y):
 area_3 = (x * y)
 return area_3

#==============================================================================

print ("Please enter the shape of which you want to find the area of: ")
print ("square = 1")
print ("triangle = 2")
print ("rectangle = 3")
print ("=============")

print ("Choose an option from 1, 2 and 3")
user_input = int(input("Please enter your option: "))

#==============================================================================

if user_input == 1:
    print ("Let's calculate the area of a square!!")
    x = float(input("Please enter the length of your desired square: "))
    area_1 = square(x)
    print ("The area of your square is: ", area_1)

#==============================================================================

if user_input == 2:
    print ("Let's calculate the area of a triangle!!")
    x = float(input("Please enter the length of your desired triangle: "))
    y = float(input("Please enter the height of your desired triangle: "))
    area_2 = triangle(x, y)
    print ("The area of your triangle is: ", area_2)

#==============================================================================

if user_input == 3:
    print ("Let's calculate the area of a rectangle!!")
    x = float(input("Please enter the length of your desired rectangle: "))
    y = float(input("Please enter the length of your desired triangle: "))
    area_3 = rectangle(x, y)
    print ("The area of your rectangle is: ", area_3)













                     
