#  set methods  

s = {3, 23, 2, 11}
print(s)
s.add(42)
s.remove(2)
# s.remove(100)  # raises KeyError: 100
s.discard(23)  # does not raise an error if the element is not present
print(s)