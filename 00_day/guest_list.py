# 1. Create an empty list to store the names
vip_guests = []

print("--- Club VIP Guest List Manager ---")
print("Type 'exit' when you are finished adding names.\n")

# 2. Start the loop to continuously collect names
while True:
    name = input("Enter a guest name: ")
    
    # 1. Check if they want to exit first
    if name.lower() == 'exit':
        break
        
    # 2. NEW VALIDATION: Check if the name contains ONLY alphabet letters
    if not name.isalpha():
        print("❌ Error: A guest name can only contain letters! Numbers or symbols are not allowed.")
        print("-----------------------------------")
        continue  # This skips the lines below and restarts the loop immediately
        
    # 3. If it passes both checks, add it to the list
    vip_guests.append(name)
    print(f"-> {name} has been added to the VIP list!")
    print("-----------------------------------")
