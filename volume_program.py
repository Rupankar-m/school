def cube(x):
 volume_1 = (x ** 3)
 return volume_1

def sphere(x):
 volume_2 = (4/3 * 3.14159 * x)
 return volume_2

def cuboid(x, y):
 volume_3 = (x * x * y)
 return volume_3

def tri_prism(x, y, z):
 volume_4 = (0.5 * x * y * z)
 return volume_4

#====================================================================================================

print ("Please enter the shape of which you want to find the volume of: ")
print ("cube = 1")
print ("sphere = 2")
print ("cuboid = 3")
print ("triangular prism = 4")
print ("====================")

print ("Choose an option from 1, 2, 3 or 4")
user_input = int(input("Enter your option: "))

#====================================================================================================

if user_input == 1:
    print ("Let's calculate the volume of a cube!!")
    x = float(input("Please enter the length of your desired cube: "))
    volume_1 = cube(x)
    print ("The area of your square is: ", volume_1)

#====================================================================================================

if user_input == 2:
    print ("Let's calculate the volume of a sphere!!")
    x = float(input("Please enter the radius of your desired sphere: "))
    volume_2 = sphere(x)
    print ("The volume of your sphere is: ", volume_2)

#====================================================================================================

if user_input == 3:
    print ("Let's calculate the volume of a cuboid!!")
    x = float(input("Please enter the width/height of your desired cuboid: "))
    y = float(input("Please enter the length of your desired cuboid: "))
    volume_3 = cuboid(x, y)
    print ("The volume of your cuboid is: ", volume_3)

#====================================================================================================

if user_input == 4:
    print ("Let's calculate the volume of a triangular prism!!")
    x = float(input("Please enter the length of the triangle in your prism: "))
    y = float(input("Please enter the height of the triangle in your prism: "))
    z = float(input("Please enter the length of your overall prism: "))
    volume_4 = tri_prism(x, y, z)
    print ("The volume of your triangular prism is: ", volume_4)
