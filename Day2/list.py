# list

# marks = [1,2,3,4,5,6,7,8,9,10]
# print(type(marks))
#
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
#
# print(f"length {len(marks)}")
#
# # we can add multiple type
#
# data = ["dev", 9898330370, "coder"]
# print(data)
#
# data[0] = "fuck"
# print(data)
#
# print(data[-2:-1])


# # list methords
#
# list  = [2,1,3]
#
# list.append(4)
# print(f"Append : {list}")
#
# list.sort()
# print(f"sort : {list}")
#
# list.sort(reverse=True)
# print(f"reverse sort :{list}")
#
# fruits = ["apple", "litchi","banana", "chicku"]
#
# fruits.sort()
# print(f"fruits sorted {fruits}")
#
# fruits.reverse()
# print(f"reverse the list: {fruits}")
#
# fruits.insert(2,"mango")
# print(f"inserting mango on index-2:{fruits}")
#
# fruits.remove("apple")
# print(f"remove object of list based on name {fruits}")
#
# fruits.pop(2)
# print(f"remove object based on index {fruits}")

# practice problem

# m1 = input("Enter 1st movie:")
# m2 = input("Enter 2st movie:")
# m3 = input("Enter 3st movie:")
#
# list = []
# list.append(m1)
# list.append(m2)
# list.append(m3)
# print(list)

# # shorter way
# movies = []
#
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2st movie: "))
# movies.append(input("Enter 3st movie: "))
# print(movies)


# solving a palindrome problem

list = [1,2,3,2,1]
list1 = [1,2,3]

copylist = list.copy()
copylist.reverse()

if (list == copylist):
    print("Palindrome")
else:
    print("Not a palindrome")

copylist1 = list1.copy()
copylist1.reverse()

if (list1 == copylist1):
    print("Palindrome")
else:
    print("Not a palindrome")