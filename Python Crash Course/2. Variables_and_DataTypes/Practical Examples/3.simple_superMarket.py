#######################################################################################
# Name of Program: PrintInfo
# author:          mr-h0n3y
# purpose:         we going to turn a simple story into small program
#######################################################################################


'''
Story:
You go to the supermarket with a list of items you need to buy:milk,
eggs, and bread. However, when you arrive, you remember that you need
to buy apples instead of bread.


1. You start with an empty shopping list.
2. You add milk to your shopping list.
3. Next, you add eggs to your shopping list.
4. You add bread to your shopping list, thinking you need it.
5. You realize you don't need bread; you need apples instead. So, you remove bread from your list and add apples.
6. Before checking out, you review your list to ensure you have everything you need: milk, eggs, and apples.
'''


# Step 1: Start with an empty shopping list
shopping_list = []

# Step 2: Add 'milk' to the shopping list
shopping_list.append('milk')

# Step 3: Add 'eggs' to the shopping list
shopping_list.append('eggs')

# Step 4: Add 'bread' to the shopping list
shopping_list.append('bread')

# Step 5: Replace 'bread' with 'apples'
shopping_list.remove('bread')  # Remove bread
shopping_list.append('apples')  # Add apples

# Step 6: Review your list
print("Final Shopping List:", shopping_list)







