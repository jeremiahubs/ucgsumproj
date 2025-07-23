



print("Welcome to the top 3 snacks collector!")

snacks = []
count = 0

while count < 4:
    snack = input(f"Enter snack #{count + 1}: ")
    snacks.append(snack)
    count += 1

print("\n Your favorite snacks are:", snacks)

snacks.sort()
print("Sorted snacks: ", snacks)

remove_item = input("\nOops! Need to remove a snack? Type one in:")

if remove_item in snacks:
    snacks.remove(remove_item)
    print("Removed snack:", remove_item)
else:
    print(" Snack not found!")

print("\n Final snack list: ", snacks)
print("Total snacks now: ", len(snacks))