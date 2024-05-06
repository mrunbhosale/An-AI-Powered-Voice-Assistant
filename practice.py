# # Day 1:

# class Rectangle:

#     def set_dimensions(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
# rect1 = Rectangle()
# rect1.set_dimensions(2, 4)
# print(rect1.area())
# print(rect1.perimeter())

# # Day 2:

# # Q1.

# class Vehicle:
    
#     def __init__(self, seat_cap):
#         self.fare = seat_cap*100

# class Bus(Vehicle):

#     def get_fare(self):
#         final_fare = self.fare + 0.1*self.fare
#         return final_fare
    
# v1 = Vehicle(50)
# b1 = Bus(50)

# print(b1.get_fare())

# # Q2.

# def division(a, b):
    
#     try:
#         c = a / b
#         print("Cleanup: Division operation completed.")
#         print(c)

#     except:
#         print("Error: Cannot divide by zero.")

# x = int(input("Enter the Dividend here: "))
# y = int(input("Enter the Divisor here: "))

# division(x, y)