
guest_list = []

user_input = input("Enter a name to add to the guest list (or 'done' to finish): ")
while user_input.lower() != "done":
    guest_list.append(user_input)
    user_input = input("Enter a name to add to the guest list (or 'done' to finish): ")

print("Guest list:", guest_list)