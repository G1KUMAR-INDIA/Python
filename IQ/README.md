### **Basic Python Programs**
1. **Even or Odd**: Check if a number is even or odd.
2. **Palindrome**: Check if a string or number is a palindrome.
3. **Prime Number**: Check if a number is a prime number.
4. **Fibonacci Series**: Generate the Fibonacci series up to `n` terms.
5. **Factorial**: Calculate the factorial of a number using recursion and iteration.
6. **Sum of Digits**: Find the sum of the digits of a number.
7. **Reverse a String**: Reverse a given string without using built-in functions.
8. **Armstrong Number**: Check if a number is an Armstrong number.
9. **Leap Year**: Determine whether a year is a leap year.

---

### **Intermediate Python Programs**
10. **Remove Duplicates from a List**: Remove duplicates from a list while maintaining order.
11. **Anagram Check**: Check if two strings are anagrams of each other.
12. **Count Vowels and Consonants**: Count the number of vowels and consonants in a string.
13. **Find the Largest Element**: Find the largest element in a list.
14. **Matrix Multiplication**: Perform matrix multiplication using nested loops.
15. **Sort a List**: Implement bubble sort or quicksort to sort a list.
16. **Binary Search**: Implement binary search on a sorted list.
17. **Find Missing Number**: Find the missing number in a given list of integers (e.g., 1 to n).
18. **GCD and LCM**: Find the GCD and LCM of two numbers.
19. **Check Substring**: Check if one string is a substring of another.

---

### **Advanced Python Programs**
20. **Find Duplicates in a List**: Identify duplicate elements in a list.
21. **Pattern Printing**: Print patterns like a pyramid, inverted pyramid, or diamond.
22. **File Operations**: Read and write data from/to a file.
23. **Check Balanced Parentheses**: Use a stack to check if parentheses are balanced.
24. **Count Words in a File**: Count the number of words or lines in a file.
25. **Generate Random Numbers**: Generate a random password or random numbers within a range.
26. **Calculate the Power of a Number**: Implement the power function without using `**`.
27. **Snake Case to Camel Case**: Convert a string from snake_case to CamelCase.
28. **Flatten a Nested List**: Flatten a list of lists using recursion or iteration.
29. **Find the Second Largest Number**: Find the second largest element in a list.

---

### **Real-World Programs**
30. **Web Scraping**: Scrape data from a website using BeautifulSoup.
31. **API Requests**: Fetch and parse JSON data from an API using `requests`.
32. **Email Validation**: Validate an email address using regular expressions.
33. **URL Shortener**: Implement a simple URL shortening service.
34. **Simple Calculator**: Build a calculator app using basic operations.
35. **Tic-Tac-Toe Game**: Create a simple two-player Tic-Tac-Toe game.
36. **CRUD Operations**: Implement CRUD operations using a SQLite database.
37. **Command-Line Arguments**: Parse and handle command-line arguments using `argparse`.
38. **Data Visualization**: Plot data using libraries like Matplotlib or Seaborn.
39. **Text Encryption and Decryption**: Implement a Caesar cipher for text encryption.

---

Here are Python programs for all **39 interview questions** listed earlier:  

---

### **1. Even or Odd**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

---

### **2. Palindrome**
```python
text = input("Enter a string: ")
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
```

---

### **3. Prime Number**
```python
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```

---

### **4. Fibonacci Series**
```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

### **5. Factorial**
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
```

---

### **6. Sum of Digits**
```python
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print(f"Sum of digits of {num} is {sum_of_digits}")
```

---

### **7. Reverse a String**
```python
text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")
```

---

### **8. Armstrong Number**
```python
num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = sum(int(digit)**order for digit in str(num))
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
```

---

### **9. Leap Year**
```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

---

### **10. Remove Duplicates from a List**
```python
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(lst))
print(f"List without duplicates: {unique_list}")
```

---

### **11. Anagram Check**
```python
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")
```

---

### **12. Count Vowels and Consonants**
```python
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
```

---

### **13. Largest Element in a List**
```python
lst = [10, 20, 30, 40, 50]
largest = max(lst)
print(f"Largest element: {largest}")
```

---

### **14. Matrix Multiplication**
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
print("Matrix multiplication result:", result)
```

---

### **15. Binary Search**
```python
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lst = [1, 3, 5, 7, 9]
target = 5
print(f"Element found at index: {binary_search(lst, target)}")
```

---

### **16. GCD and LCM**
```python
import math
a, b = 12, 18
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print(f"GCD: {gcd}, LCM: {lcm}")
```

---

### **17. Balanced Parentheses**
```python
def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or {")": "(", "}": "{", "]": "["}[char] != stack.pop():
                return False
    return not stack

expression = "{[()]}"
print(f"Balanced: {is_balanced(expression)}")
```

---

### **18. Find Missing Number**
```python
lst = [1, 2, 4, 5]
n = len(lst) + 1
missing_number = n * (n + 1) // 2 - sum(lst)
print(f"Missing number: {missing_number}")
```

---

### **19. Pattern Printing**
```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```

---

### **20. Flatten a Nested List**
```python
def flatten(lst):
    flat_list = []
    for i in lst:
        if isinstance(i, list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list

nested_list = [1, [2, [3, 4]], 5]
print(flatten(nested_list))
```

Continuing with the remaining Python programs:  

---

### **21. Transpose of a Matrix**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transpose of the matrix:")
for row in transpose:
    print(row)
```

---

### **22. Count Occurrences of an Element in a List**
```python
lst = [1, 2, 3, 1, 2, 1, 4, 5]
element = 1
count = lst.count(element)
print(f"{element} occurs {count} times in the list.")
```

---

### **23. Check Perfect Number**
```python
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
```

---

### **24. Check Strong Number**
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
if num == sum_of_factorials:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
```

---

### **25. Find HCF**
```python
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = 60, 48
print(f"HCF of {a} and {b} is {hcf(a, b)}")
```

---

### **26. Decimal to Binary Conversion**
```python
num = int(input("Enter a decimal number: "))
binary = bin(num)[2:]
print(f"Binary representation of {num} is {binary}")
```

---

### **27. Calculate Power Without `**`**
```python
base, exp = 2, 3
result = 1
for _ in range(exp):
    result *= base
print(f"{base} to the power of {exp} is {result}")
```

---

### **28. Find Duplicates in a List**
```python
lst = [1, 2, 3, 1, 2, 4]
duplicates = set([x for x in lst if lst.count(x) > 1])
print(f"Duplicates: {duplicates}")
```

---

### **29. Check Pangram**
```python
import string
text = input("Enter a sentence: ")
if set(string.ascii_lowercase).issubset(set(text.lower())):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
```

---

### **30. Merge Two Sorted Lists**
```python
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged = sorted(lst1 + lst2)
print(f"Merged list: {merged}")
```

---

### **31. Find Second Largest in a List**
```python
lst = [10, 20, 4, 45, 99]
unique_sorted = sorted(set(lst))
second_largest = unique_sorted[-2]
print(f"Second largest element is {second_largest}")
```

---

### **32. Convert String to Integer**
```python
num_str = "12345"
num = int(num_str)
print(f"Converted integer: {num}")
```

---

### **33. Count Words in a String**
```python
text = "This is a sample string with several words"
word_count = len(text.split())
print(f"Number of words: {word_count}")
```

---

### **34. Find Intersection of Two Lists**
```python
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
intersection = list(set(lst1) & set(lst2))
print(f"Intersection: {intersection}")
```

---

### **35. Generate Random Number**
```python
import random
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")
```

---

### **36. Calculate Compound Interest**
```python
P = 1000  # Principal
R = 5     # Rate of interest
T = 2     # Time in years
A = P * (1 + R / 100) ** T
print(f"Compound Interest is {A - P}")
```

---

### **37. Check Substring**
```python
string = "hello world"
substring = "world"
if substring in string:
    print(f"'{substring}' is a substring of '{string}'")
else:
    print(f"'{substring}' is not a substring of '{string}'")
```

---

### **38. Sort Dictionary by Value**
```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(f"Sorted dictionary: {sorted_dict}")
```

---

### **39. Find Length of a Linked List**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(f"Length of the linked list: {ll.length()}")
```

```