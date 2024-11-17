# Initialize an empty list for food items
foods = []

# Get the number of food items
n = int(input("Enter the number of food items to consider: "))

# Get the details for each food item
for i in range(n):
    print(f"\nEnter details for food item {i + 1}:")
    food_name = input("Food name: ")
    calories = int(input("Calories: "))
    cost = float(input("Cost (in dollars): "))
    nutrition_value = int(input("Nutrition value (e.g., protein, vitamins): "))
    # Add the food item as a tuple to the list
    foods.append((food_name, calories, cost, nutrition_value))

# Get the user's calorie, budget, and nutrition requirements
calorie_limit = int(input("\nEnter your maximum calorie limit for the meal plan: "))
budget_limit = float(input("Enter your maximum budget for the meal plan (in dollars): "))
required_nutrition = int(input("Enter the minimum required nutrition value: "))

# Number of food items
n = len(foods)

# Initialize a DP table for calorie and budget constraints
# dp[i][calories][budget] stores the maximum nutrition achievable with i items, given calorie and budget limits
dp = [[[0 for _ in range(int(budget_limit * 100) + 1)] for _ in range(calorie_limit + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    food_name, calories, cost, nutrition_value = foods[i - 1]
    for c in range(calorie_limit + 1):
        for b in range(int(budget_limit * 100) + 1):  # Converting budget to cents to avoid float issues
            if calories <= c and int(cost * 100) <= b:
                dp[i][c][b] = max(dp[i - 1][c][b],
                                  dp[i - 1][c - calories][b - int(cost * 100)] + nutrition_value)
            else:
                dp[i][c][b] = dp[i - 1][c][b]

# Check if the maximum nutrition meets the required nutrition
max_nutrition = dp[n][calorie_limit][int(budget_limit * 100)]
if max_nutrition < required_nutrition:
    print("It's not possible to meet the required nutrition within the given calorie and budget limits.")
else:
    print(f"\nMaximum Nutrition Value Achievable: {max_nutrition}")

    # Backtrack to find selected food items
    selected_foods = []
    c = calorie_limit
    b = int(budget_limit * 100)
    for i in range(n, 0, -1):
        if dp[i][c][b] != dp[i - 1][c][b]:  # This food item was included
            food_name, calories, cost, nutrition_value = foods[i - 1]
            selected_foods.append(food_name)
            c -= calories
            b -= int(cost * 100)

    print("Selected Foods for Optimal Meal Plan:", selected_foods)
