# Pass  statement is used when you want to write a loop but you don't want to do anything in it. It is a placeholder that allows you to write code that will be executed later. When the pass statement is executed, it does nothing and simply moves on to the next iteration of the loop. This can be useful when you are still working on the logic of your loop and want to avoid syntax errors.

i = 1
while i <= 10:
    pass  # This will do nothing and simply move on to the next iteration of the loop
    i += 1
print("Loop has completed.")

