# list methods
# lists have built-in methods that allow us to perform various operations on them   

marks = [85, 90, 78, 92, 88]
extra_marks = [30,40,50]
print(marks)  # Output: [85, 90, 78, 92, 88]
marks.append(95)  # adds an element to the end of the list
print(marks)  # Output: [85, 90, 78, 92, 88, 95]

marks.pop()  # removes and returns the last element of the list
print(marks)  # Output: [85, 90, 78, 92, 88]

marks.insert(2, 80)  # inserts an element at a specific index
print(marks)  # Output: [85, 90, 80, 78, 92, 88]

marks.extend(extra_marks)  # extends the list by appending elements from another list
print(marks)  # Output: [85, 90, 80, 78

marks.remove(78)  # removes the first occurrence of a specific element
print(marks)  # Output: [85, 90, 80, 92, 88, 30, 40, 50]

marks.sort()  # sorts the list in ascending order
print(marks)  # Output: [30, 40, 50, 80, 85, 88, 90, 92]