import time

def get_meal_calories(meal_name):
    print(f"--- Adding items for: {meal_name} ---")
    total_calories = 0
    # for item counting
    while True:
        num_items_str = input("How many food items? ")
        if num_items_str.isdigit():
            # loop for evry food item
            for i in range(int(num_items_str)):
                food_name = input(f"  Item {i + 1}: ")
                # for colorie numberss
                while True:
                    calories_str = input(f"    Calories for {food_name}: ")
                    if calories_str.isdigit():
                        # calories ko total me add kar diya
                        total_calories += int(calories_str)
                        break
                    print("    Please enter a number.")
            # for final calories wapas
            return total_calories
        print("Please enter a number.")


print(" Kcal Tracker ")
# list for saving mels
daily_log = []

# how many meals to put in for that loop
while True:
    total_meals_str = input("How many meals to log? ")
    if total_meals_str.isdigit():
        total_meals = int(total_meals_str)
        break
    print("Please enter a valid number.")

# for every meal thius is the loop
for i in range(total_meals):
    print()
    meal_name = input(f"Name for meal #{i + 1}: ")

    # for current timme
    current_time = time.strftime("%I:%M %p")
    print(f"Time logged: {current_time}")

    # for colorie
    calories = get_meal_calories(meal_name)
    # every info saved form dic to list
    daily_log.append({"name": meal_name, "time": current_time, "calories": calories})


grand_total = sum(meal['calories'] for meal in daily_log)  # for total colorie

#  UPDATED TABULAR SUMMARY 
print("\n--- Your Daily Summary ---")
# Print the table headers with fixed widths
print(f"{'Time':<12} {'Meal':<18} {'Calories'}")
print("-" * 42)  # A separator line for the table

average_calories = grand_total / total_meals

# for printing every meals details
for meal in daily_log:
    # Print each row  ensuring each part fits into its column
    print(f"{meal['time']:<12} {meal['name']:<18} {meal['calories']} kcal")

print("-" * 42)  # Another separator line
# Format the final line to align with the table
print(f"{'Total Calories:':<31} {grand_total} kcal")
print(f"{'Average per Meal:':<31} {average_calories:.2f} kcal")
