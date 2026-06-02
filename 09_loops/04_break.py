#  break   
#  break is used to exit a loop prematurely, before it has completed all iterations. When the break statement is executed, the loop is immediately terminated, and the program continues with the next statement after the loop. This can be useful when you want to stop a loop based on a certain condition or when you have found what you were looking for and no longer need to continue iterating.

for i in range(0, 21):
    if i == 11:
        break  # This will exit the loop when i is equal to 11
    print(i)