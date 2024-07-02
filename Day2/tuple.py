# tuple are immutable

list = (1,2,3,4,2,2,2,2,2,)
print(f"this is type of tuple{type(list)}")

print(list[0])
print(list[1])

print(list[1:2])

print(f"returns index of first occurance : {list.index(2)}")
print(f"count the no. of time occurance : {list.count(2)}")
