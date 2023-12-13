#Exercise 3: Is it Triangle:
#Write a program that asks the user to enter the lengths of the three sides of a triangle. Use the triangle inequality to determine if we have a triangle: In mathematics, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side (see here)

#Extension Problem (Optional):If valid, ask the user for the length of the sides and have the program correctly classify the type of triangle as either: Equilateral, Isosceles or Scalene (see here)    



#asking user to type 3 numbers
print("Enter 3 numbers for the triangle")
#taking 3 user inputs
a=int(input("First angle: "))
b=int(input("Second angle: "))
c=int(input("Thrid angle: "))

#checking if it is a triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    print("\nIt is a triangle:")
    #if it is a triangle then checking what type of triangle it is with nested if statements
    #if all sides are equal
    if a==b==c:
        print("Equilateral")
    #if two sides are equal
    elif a==b or b==c or a==c:
        print("Isosceles")
    #if no sides are equal
    else:
        print("Scalene")
        
#if it is an invalid triangle
else:
    print("it is not a triangle")