# n = 10
# try:
#     res = n / 0
# except ZeroDivisionError:
#     print("Can't be divided by zero!")

###################################################

# try:
#     n = 0
#     res = 100 / n
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# except ValueError:
#     print("Enter a valid number!")
    
# else:
#     print("Result is", res)
    
# finally:
#     print("Execution complete.")


###################################################

# try:
#     # Risky operation: dividing string by number
#     res = "100" / 20 
    
# except ArithmeticError:
#     print("Arithmetic problem.")
    
# except:
#     print("Something went wrong!")

###################################################

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)