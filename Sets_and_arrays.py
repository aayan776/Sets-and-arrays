import array as arr
#Adding
set1 = {1,1,2,3,4,5,5,6}
print(set1)
set1.add(7)
print(set1)
set1.add(7)
print(set1)
#Different things in sets
set_int = {1,2,3,4}
print(f"Sets can have integers: {set_int}")
set_multi = {1.0, "Hello", (1,4,3,2)}
print(f"Sets can have multiple types of data: {set_multi}")
set_list = set([1,2,3,4,5])
print(f"Lists can be sets: {set_list}")
#Union method
set2 = {"Math", "English", "Chemistry"}
set3 = {"Math", "English", "Physics"}
union_set_1 = set2.union(set3)
union_set_2 = set2 | set3
print(union_set_1)
print(union_set_2)
#Intersection
set_intersection_1 = set2.intersection(set3)
set_intersection_2 = set2 & set3
print(set_intersection_1)
print(set_intersection_2)
set4 = {"Blue", "Yellow"}
set5 = {"Blue", "Green"}
print(f"Original sets: {set4}, {set5}")
set6 = set4.intersection(set5)
print(f"Intersected set: {set6}")
#Array
a = arr.array("b", [1,2,3,4])
print("Array: ")
for i in range(0, 4):
    print(a[i])
print()
#Array insert and append
b = arr.array("d", (1.0, 2.0, 3.0, 4.0))
print(f"Array: {b}")
b.insert(4, 5.0)
print(f"Array after insertion: {b}")
b.append(5.1)
print(f"Array after appending: {b}")
#Array concatination
c = arr.array("i", [1,3,5,8,12,5,234])
print("Array: " + str(c))
#Array reverse
c.reverse()
print(f"Revesed array: {c}")