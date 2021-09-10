
x=10
y="Y Variable"
print(x,'and',y)
print(x, end = ". ")
print('The value of x is', x)

d=input()
print("D is", d)

print("D is", input())

f=input("Enter Integer Only : ")
print(f)

'''
int x; # Declaration
x = 9; # Initialisation
int x = 9; # Both Together
'''

x=1
print(type(x))
x=1.0
print(type(x))

#Operators
#Arithmetic Operators
x = 10
x += 15     # x=x+15
print(x)
x -= 1     # x=x-1
print(x)
x *= 2     # x=x*2
print(x)
x /= 2     # x=x/2
print(x)
x %= 9    # x=x%4
print(x)
x //= 3    # x=x//3
print(x)
x **= 3    # x=x**3
print(x)


# Conditional Statements
x = 5
print(x > 3)
print(x < 3)
print(x >= 3)
print(x <= 3)
print(x == 3)
print(x != 3)


# Logical Operators
x = 6 
y = 3
print((x<5) and (y<5))
print((x>5) or (y<5))
print(not (x>5))

# Bitwise Operator
print(2 | 9)   # AND
print(5 & 9)   # OR
print(6 ^ 9)   # XOR
print(8 >> 2)  # Shift Right
print(8 << 2)  # Shift Left

# Identity Operator
x = 5
print(x is 6)
print(x is not 6)

# Membership Operator
x = [1,2,3,4,"a"]
print(4 in x)
print('a' not in x)

# Conditional Statements
x = 5
# Nested If
if x < 7 :
    print("If Conditon Satisfied")
elif x < 11:
    print("Elif Condition Satisfied")
else:
    print("Else Condition Satisfied")
print("OUT")

# Ladder If
if x < 7 :
    print("If Conditon Satisfied")
if x < 11:
    print("Elif Condition Satisfied")
else:
    print("Else Condition Satisfied")
print("OUT")

print("Hey") if x < 5 else print("Hoi")


