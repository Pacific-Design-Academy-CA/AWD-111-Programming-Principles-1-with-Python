# Programming Principles 1 (#2)

> If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger Dijkstra, computer science pioneer
> 

# 🔄 Recap of last day

- Python Rules & Syntax
- Variables
- Functions

# ⛅ Today’s topic

- Data types
- Input & Output
- Assignment 1
- Exercises

# 🧑🏾‍🔬 Data types in Python

![Untitled](Programming%20Principles%201%20(#2)%2035310798695145688474183525a5a783/Untitled.png)

🔍**Getting the data type:**

```python
x = 5
print(type(x))
```

📤 **Output:**

```python
<class 'int'>
```

# 📇 Input & Output in Python

For today’s class we are going to look at input and output in python,

```python
# Taking input from the user
name = input("Enter your name: ")
 
# Output
print("Hello, " + name)
print(type(name))
```

📤 **Output:**

```python
Enter your name: GFG
Hello, GFG
<class 'str'>
```

<aside>
💡 **Note:** 
Python takes all the input as a string input by default. To convert it to any other data type we have to convert the input explicitly. For example, to convert the input to int or float we have to use the **[int()](https://www.geeksforgeeks.org/python-int-function/)** and **[float()](https://www.geeksforgeeks.org/float-in-python/)** method respectively.

</aside>

## 🗒️ Integer input in Python

```python
# Taking input from the user as integer
num = int(input("Enter a number: "))
 
add = num + 1
 
# Output
print(add)
```

## 📤 Output

```python
Enter a number: 25
26
```

## 🎰 Taking multiple inputs in python

```python
a, b, c = map(int, input("Enter the Numbers : ").split())
print("The Numbers are : ",end = " ")
print(a, b, c)
```

## 📤 Output

```python
Enter the Numbers : 2 3 4
The Numbers are :  2 3 4
```

# 🖨️Displaying Output in Python

```python
# Python program to demonstrate
# print() method
print("GFG")
 
# code for disabling the softspace feature 
print('G', 'F', 'G')
```

## 📤Output:

```python
GFG
G F G
```

## 😎 Cool feature:

```python
# Python program to demonstrate
# print() method
print("GFG", end = "@")
 
# code for disabling the softspace feature 
print('G', 'F', 'G', sep="#")
```

# Exercises:

1. What is the output of the following code?

```python
# airfare.py
age = int(input('How old are you? '))
if age <= 2:
    print(' free')
elif 2 < age < 13:
    print(' child fare)
else:
    print('adult fare')
```

1. The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
    1. The first line contains the sum of the two numbers.
    2. The second line contains the difference of the two numbers (first - second).
    3. The third line contains the product of the two numbers.

```python
#complete this

a = int(input())
b = int(input())
```

# References:

- [https://www.geeksforgeeks.org/input-and-output-in-python/](https://www.geeksforgeeks.org/input-and-output-in-python/)
- [https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp)
