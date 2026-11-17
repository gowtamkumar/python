

# list comprehension
# names = ["gowtam kumar", "rahul kumar", "amit"]

# upper_names = [name for name in names if 'kumar' in name]

# print(upper_names)

## set comprehension
# colors = ["red", "green", "yellow", "blue", "red", "green", "blue"]
# unique_color = {color for color in colors if len(color) < 5}
# print(unique_color)

# recipes = {
#     "Pasta": ["pasta", "tomato sauce", "cheese"],
#     "Salad": ["lettuce", "tomato", "cucumber", "dressing"],
#     "Pizza": ["dough", "tomato sauce", "cheese", "toppings"],
# }
# unique_ingredients = {recipe for ingredients in recipes.values() for recipe in ingredients }
# print(unique_ingredients)

# # dictionary comprehension
# tea_prince_bdt = {
#     "masala Chai": 40,
#     "Green tea": 50,
#     "Lemon Tea": 100
# }

# tea_prince_usd = {tea:price / 122 for tea, price in tea_prince_bdt.items()}

# print(tea_prince_usd)

# generator compreshension

daily_sales = [33,44,566,222,332,100]
total_cups = sum(sale for sale in daily_sales if sale > 50)
print(total_cups)
# ......................
# numbers = [1, 2, 3, 4, 5]
# # Comprehension Without Condition
# result = []
# for number in numbers:
#     result.append(number * 3)
# print(result)
# # Comprehension With Condition
# res_com = [number * 3 for number in numbers]
# print(res_com)

# even_odd = [number for number in numbers if number % 2 == 0]

# print(even_odd)

# expenses = [ 
#     {"id": 1, "title": "Lunch", "amount": 250},
#     {"id": 2, "title": "Uber", "amount": 380},
#     {"id": 3, "title": "Laptop", "amount": 50000},
#     {"id": 4, "title": "Shopping", "amount": 3000},
# ]

# title = [expense["title"] for expense in expenses]
# print(title)

# # Conditional transformation:
# # [value_if_true if condition else value_if_false for x in numbers]
# show_string = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

# print(show_string)

# # Nested Loops in Comprehension
# numbers = [1, 2, 3]
# letters = ["A", "B"]

# result = []

# for number in numbers:
#     for letter in letters:
#         result.append((number, letter))

# res = [(number, latter) for number in numbers for latter in letters]

# print(res)

# # Nested List Comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# rest = [number for row in matrix for number in row]

# print(rest)

# # Set Comprehension
# numbers = [1, 2, 2, 3, 3, 4]

# unique = {number for number in numbers}

# print(unique)
# # Generator Expression

# numbers = [1, 2, 3, 4, 5]

# result = [number * 2 for number in numbers]

# # sum() + Comprehension
# expenses = [
#     {"title": "Lunch", "amount": 250},
#     {"title": "Uber", "amount": 380},
#     {"title": "Shopping", "amount": 3000},
# ]


# total = sum(expense["amount"] for expense in expenses)

# print("total", total)
