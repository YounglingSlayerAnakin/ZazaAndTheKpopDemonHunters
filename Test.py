import csv

while True:
    food_choice = input("\nWhat is your favorite food? ")
    matches = []

    with open('food_list.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check for partial match in the Meal_Name column
            if food_choice.lower() in row['Meal_Name'].lower():
                matches.append(row) # Store the whole row (dictionary)

    # Scenario 1: No matches
    if len(matches) == 0:
        print(f"Sorry, '{food_choice}' was not found. Please try again.")

    # Scenario 2: Perfect match!
    elif len(matches) == 1:
        selected = matches[0]
        print(f"\n--- Food Found! ---")
        print(f"Meal:     {selected['Meal_Name']}")
        print(f"Category: {selected['Category']}")
        print(f"Cuisine:  {selected['Cuisine']}")
        break # Exit the loop

    # Scenario 3: Multiple matches
    else:
        print(f"\nWe found {len(matches)} options for '{food_choice}':")
        for item in matches:
            print(f" - {item['Meal_Name']}")
        print("Please be more specific (e.g., type the full name).")

print("\nSearch complete.")

