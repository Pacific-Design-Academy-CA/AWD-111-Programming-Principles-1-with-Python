import sys

#print(sys.version)

statement1 = "Hello World"

y = len(statement1)

statement2 = "Hello World has less than 20 characters"
statement3 = "I am in the middle"
print(x);

print("Hello World")

statement1 = "Hello World"

y = len(statement1)

statement2 = "Hello World has less than 20 characters"
statement3 = "I am in the middle"
# print(x);
#parent statement
if y > 20:
    #child statement
    print(statement1)
elif y < 12:
    print(statement3)
    print(statement1)  
else:
    print(statement2)
