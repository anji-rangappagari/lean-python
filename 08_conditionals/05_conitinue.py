#  continue statement is used to skip the current iteration of a loop and move on to the next one. When the continue statement is executed, the rest of the code inside the loop for that iteration is ignored, and the loop proceeds to the next iteration. This can be useful when you want to skip certain iterations based on a condition or when you want to avoid executing certain code for specific cases.

# for i in range(0, 21):
#     if i == 11:
#         continue  # This will skip the rest of the code in the loop when i is equal to 11 and move on to the next iteration
#     print(i)


for i in range (0,100):
    if i % 2 == 0:
        continue  # This will skip the rest of the code in the loop for even numbers and move on to the next iteration
    print(i)