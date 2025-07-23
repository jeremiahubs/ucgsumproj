

foods = ["Pizza", "Tacos", "Burgers", "Sushi", "Fries"]
print(" Starting Food List:", foods)

new_food = input("Enter one food to add to the list:")
foods.append(new_food)
print("Added! New List:", foods)

remove_food = input("Enter a food you want to remove form the list:")
if remove_food in foods:
    foods.remove(remove_food)
    print(f"Removed {remove_food}.")
else:
    print(f" {remove_food} is not in the list.")
print(" Current list:", foods)

print("Total items in the list", len(foods))

should_sort = input(" Do you want to sort the list alphabetically? (yes/no)").lower()
if should_sort == "yes":
    foods.sort()
    print("Sorted List:", foods)
else:
    print("Skipping sort. Final list remains:")
    print(foods)