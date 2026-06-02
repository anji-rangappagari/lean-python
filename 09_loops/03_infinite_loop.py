#  infinite loop is a loop that continues to execute indefinitely because the loop's terminating condition is never met. This can
# happen when the condition is always true or when there is no condition at all. Infinite loops can be intentional, such as in the case of a server that needs to run continuously, or unintentional, which can lead to a program crashing or consuming excessive resources.

# Example of an intentional infinite loop:
# while True:
#     print("This loop will run forever!")

i = 1
while True:
    print(i)
    i = i + 1  # This line is commented out, so the value of i will never change, resulting in an infinite loop.