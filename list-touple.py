# Create a list of 10 integers and print:
# list = [2,3,4,5,6,7,8,9,0,11]
# # print(list)
# # # first element
# # print(list[0])
# # # last element
# # print(list[-1])
# # middle element
# # Find middle index
# middle_index = len(list) // 2

# # Print middle element
# print("Middle element:", list[middle_index])

# Reverse a list without using built-in functions.
# li = [2,4,6,7,8,9,0,]
# a = []
# for i in range(len(li)-1,-1,-1):
#     a.append(li[i])

# print(a)
# Count how many times a specific element appears in a list.
# /////////////////////////////////////////


# # Find the maximum and minimum number in a list.
# li = [10,20,90,100,900,500]
# li.sort()
# print(li[0],li[-1])
# Remove duplicates from a list.
# list = [20,30,60,20,10,80,90]
# list2 = []
# for num in list:
#     if num not in list2:
#         list2.append(num)
# # print(list2)


# # Check if a list is empty or not.
# list = []
# if not list:
#     print("list empty hai")
# else:
#     print("list empty mhi hai")

# # Swap first and last elements of a list.
# li = [10,20,30,40,50,60,70,80,90]
# li[0], li[-1] = li[-1], li[0]
# print(li)

# Find the second largest number in a list.
# li = [ 22,44,66,88,99,333,]
# li.sort()
# print(li[-2])
# Merge two lists and sort them.
# li1 = [2,3,4,5,6]
# li2 = [7,8,9,10,11]
# li3 = []
# li3 =li1 + li2
# li3.sort()
# print(li3)
# Find all even numbers from a list.
# li = [2,3,4,5,6,7,8,99,10]
# li2 = []
# for i in li:
#     if i % 2 == 0:
#         li2.append(i)
# print(li2)

# # Create a new list with squares of each element.
# li = [2,5,6,8,9,]
# li2 = []
# for num in li:
   
#     li2.append(num*num)
# print(li2)
# Find common elements between two lists.
# li = [2,4,6,8,10]
# li2= [3,5,2,8,6,]
# li3 = []

# for i in li:
#     for f in li2:
#         if i == f:
#             li3.append(i)
#             break   # important

# print(li3)

 
# # Rotate a list to the right by 1 position
# # Example:
# # [1,2,3,4] → [4,1,2,3]
# li = [1, 2, 3, 4]

# last = li[-1]       
# rest = li[:-1]       

# rotated = [last] + rest

# print(rotated)

# Split a list into two halves.
# li = [1, 2, 3, 4, 5, 6]

# mid = len(li) // 2
# a = li[:mid]
# b = li[mid:]
# print(a)
# print(b)
# Flatten a nested list
# Example:
# [[1,2],[3,4]] → [1,2,3,4]
# li = [[1,2],[3,4]]

# flat = []

# for i in li:
#     for f in i:
#         flat.append(f)

# print(flat)

# 🔹 Advanced Level
# Find the frequency of each element
# li = [2,4,6,8,3,5,7,8,2,5]
# a = {}
# for num in li:
#     if num in a :
#         a[num] += 1
#     else:
#         a[num] = 1
# print(a)

# Find the longest increasing sublist
# Check if a list is a palindrome
# li = [222,222,222,222,222,222]
# start = 0
# end = len(li) -1
# new = True

# while start < end :
#     if li[start] != li[end] :
#         new = False
#     start += 1
#     end -= 1
# if new:
#     print("palindrome hai")
# else:
#     print("palindrome nhi hai")


 

# Find all pairs with a given sum
# Example:
# list = [1,2,3,4], sum=5 → (1,4),(2,3)
# li = [2,3,4,1,4,4,2,3,1,4]
# target = 5
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i] + li[j] == target:
#             print(li[i],li[j])


# Implement list compression
# Example:
# [1,1,1,2,2,3] → [(1,3),(2,2),(3,1)]
# li = [1,1,1,2,2,3]

# result = []
# # count = 1

# # for i in range(1, len(li)):
# #     if li[i] == li[i-1]:
# #         count += 1
# #     else:
# #         result.append((li[i-1], count))
# #         count = 1

# # # last element add करना जरूरी है
# # result.append((li[-1], count))

# # print(result)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Sort a list without using sort() or sorted()
# li = [31,38,54,15,18,19,20]
# num = 2
# for num in range(len(li)):
    

# # 1. Check if a Tuple is Empty
# t = ()
# if not t:
#     print("empty")
# else:
#     print("not empty")

# # 2. Find Maximum and Minimum Element
# t = (2,5,6,7,8,3,2,4,6,)


# print("Maximum:", max(t))
# print("Minimum:", min(t))

# 3. Convert Tuple to List and Modify
touple = (3,5,7,8,9,6,44,2,4,5,6)
li = [touple]
print(li)
print(type(li))


