# # Print numbers from 1 to N
# n = int(input("enter any number :"))
# for i in range(1,n+1):
#     print({i})

# # Print numbers from N to 1 (reverse)
# n = int(input("enter any number :"))
# for i in range(n,-1,-1):
#     print({i})

# Print even numbers from 1 to N
# n = int(input("enetr any number :"))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(f"{i} even")
# Print odd numbers from 1 to N

# # Print multiplication table of a number
# num = int(input("enetr any number "))
# for i in range(1,11):
#     print(f"{num * i }")

# # Find sum of first N numbers
# n = int(input("enetr any number :"))
# a = 0
# for i in range(1,n+1):
#       a = i + a
#       print({a})

# Find factorial of a number
# n = int(input("Enter number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("Factorial =", fact)


# # Count digits in a number
# num = int(input("enter any  number:"))
# count = 0 
# for i in range(1,num+1):
#     count += i
#     print({count})

# # Reverse a number
# num = int(input("enter any  number:"))
# reverse = 0
# digit = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#     print(f"{reverse}")
    
    

# Check palindrome number

# Sum of digits
# num = int(input("enter any number: "))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print("Sum of digits =", sum)

# Product of digits
# num = int(input("enter any number :"))
# product = 1

# while num > 0:
#     digit = num % 10
#     product = product * digit
#     num = num // 10

# print("product of digit =" , product)

# Find largest digit in number

# num = int(input("enter the number: "))
# largest = 0

# while num > 0:
#     digit = num % 10
    
#     if digit > largest:
#         largest = digit
    
#     num = num // 10

# print("Largest digit =", largest)

# Prime number check
# num = int(input("enter any number: "))

# for i in range(2, num):
#         if num % i == 0:
#             print("composite number")
#             break
# else:
#         print("Prime number")


# Print all prime numbers between 1 to N
# num = int(input("enter any number :"))
# a =  0
# for i in range(2,num):
#    if num % num == 0:
#     break
# print(f"{num} prime")




# # Fibonacci series
# n = int(input("Enter number: "))
# a = -1
# b = 1
# c = 0
# for i in range(1,n+1):
#     c = a+ b
#     print(c)
#     a = b
#     b = c


# # Armstrong number
# num = int(input("enter any number"))
# orignal = num
# for i in range(1,num):
#     if num * 3 and num == orignal:
#         print(f"armstrong")
#         break
# else:
#     print(f"not....")

# # ✅ 3. Sum of first N numbers
# num = int(input("enter any number :"))
# sum = 0 
# for i in range(1,num+1):
#     sum +=  i
# print(sum)

# ✅ 4. Multiplication table
# num = int(input("enter any number: "))
# for i in range(1,11):
#  print(f"{num * i}")

# # ✅ 5. Factorial of a number ⭐
# num = int(input("enter any number :"))
# fac = 1
# for i in range(1,num+1):
#  fac *= i
#  print(i)
# print(fac) 

# # ✅ 6. Count digits in a number ⭐
# num = int(input("enter any number:"))
# count = 0
# while num > 0 :
#     num //= 10 
#     count += 1
# print(count)    

# . Reverse a number ⭐
# num = int(input("enter  any number :"))
# rev = 0
# while num > 0 :
#     digit = num % 10 
#     rev= rev* 10 + digit
#     num //= 10
# print(rev)    

# # ✅ 8. Palindrome number ⭐
# num  = int(input("enter any number :"))
# original = num 
# rev = 0
# while num > 0 :
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10 
# if original == rev:
#     print(f"palindrom{rev}")
# else:
#     print(f"not palindrome{rev}")

# # 9. Prime number ⭐ (important)
# num = int(input("ente any number :"))
# for i in range(2, num):
#     if num % i == 0:
#         print("not prime ")
#         break
# else:
# #     print("prime")


# # 1 se 100 tak saare prime numbers print karo
# for num in range(10, 101):
#     for i in range(11, num):
#         if num % i == 0:
#             break
#     else:
#        if num % 2 == 0:
#         print(num)
        


# 👉 Print:

# sirf even prime numbers
# sirf 2 digit prime numbers

# 3-digit prime numbers (100–999)


# count kitne 3-digit prime numbers hain

# count = 0
# num = 2
# sum = 0

# while count < 50:
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         # print(num)
#         count += 1
#         sum += num 
#     num += 1
# print(sum)
    




# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# 🚀 Mini Project: Prime Number Analyzer
# 🎯 Project kya karega?

# User se number lega aur:

# Check karega → prime hai ya nahi
# # 1 se us number tak saare prime print karega
# # total prime count batayega
# # unka sum bhi batayega

# num =  int(input("enter any number :"))                           
# count = 0 
# total = 0
# for n in range (2,num+1):
#     for i in range(2,n):
#         if n % i == 0:
#         #  print("...")
#          break
#     else:
#         print(n, "is prime")
#         count += 1
#         total += n


# print("sum:",total)
# print("total primes :", count)


    

