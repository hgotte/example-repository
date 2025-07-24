##################################
# ---- Type hinting example ---- # 
##################################

# Python 2, lots of syntax

name: str = "Peter"

if  name == "Peter":
    print("Hello, this is english Peter!")
elif name == "Petr":
    print("Hello, this is czech Petr!")
elif name == "Pietro":
    print("Hello, this is italian Pietro!")
elif name == "Pierre":
    print("Hello, this is french Pierre!")
else:
    print("Hello, this is unknown Peter!")

def add_numbers(a=1, b=2)
    return a + b
    
result = add_numbers(3, 4)

print("The result of the addition is:", result)