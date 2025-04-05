word = input("Enter a word: ")
if word == word[::-1]:
    print("The given String is Palindrome.")

else:
    print("The given String is Not Palindrome.")

"""**************************************************************************"""
words = 'Capitalize the First Letter of Each Word'
print(words.title())

"""**************************************************************************"""
"""Return an Array of Even Numbers (without filter or forEach)"""
num = [10,12,13,13,44,22,]
even = []
i=0
while i < len(num):
    if num[i] % 2 == 0:
        even.append(num[i])
    i += 1
print(even)
"""**************************************************************************"""
""" Find Sum of Two for Target Sum"""
def sum_of_two_nums(arr1, targeta):
    for n1 in range(len(arr1)):
        for n2 in arr1[n1::1]:
            if n1+n2 == targeta:
                return f"the two numbers are {n1} & {n2}."
    pass
arr = [1,2,3,4,5,6,7,8,9,10]
targetb = 15
print(sum_of_two_nums(arr, targetb))
"""**************************************************************************"""
'''13. Find Length of Longest Substring Without Repeating Characters'''
word = 'abcdabcaamnspouy'
new = []
final =""
for r in word:
    if r not in final:
        final += r
    else:
        new.append(len(final))
        final = final[final.index(r) + 1:] + r
        print(final)
new.append(len(final))
print(new)
print(max(new))
"""**************************************************************************"""
"""Find the nth Fibonacci Number (using Recursion)"""
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
num = 10
print(fibonacci(num))
# arr =[0,1]
# for i in range(1,num):
#     arr.append(arr[-2]+arr[-1])
# print(arr[-1])
"""**************************************************************************"""
'''Sum of First 100 Prime Numbers'''
arr=[]
i =2
while len(arr)< 100:
    is_prime = True
    for k in range(2, i//2 +1):
        if i%k ==0:
            is_prime = False
    if is_prime:
        arr.append(i)
    i+=1
print("First 100 prime numbers:", arr)
print("Sum:", sum(arr))
"""**************************************************************************"""
''' Generate Multiples of a Number (Given Length)'''
num = int(input("Enter number: "))
length = int(input("Enter Length: "))
for i in range(1, length+1):
    print(f"{num} * {i} = {num*i}")

"""**************************************************************************"""
'''FizzBuzz'''
def fizzBuzz(num):
    if num%3 == 0  and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
fizzBuzz(15)
"""**************************************************************************"""
'''20. Repeat Each Character in a String'''
def repeat(w):
    return ''.join([k*2 for k in w])
string = input("Enter a String: ")
print(repeat(string))