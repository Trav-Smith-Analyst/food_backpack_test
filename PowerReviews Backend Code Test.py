#!/usr/bin/env python
# coding: utf-8

# In[25]:


# def is used to define the function.
# food_backpack is the name of the function.
# bag_capacity is a parameter that the function expects when it is called.

def food_backpack(bag_capacity):
    items_available = [
        {"name": "Bag of Apples", "weight": 5},
        {"name": "Trail Mix", "weight": 3},
        {"name": "Peanut Butter", "weight": 2},
        {"name": "Bread", "weight": 1},
    ]
    
    
    # First, add one of each item to the backpack
    backpack = []
    for item in items_available:
        backpack.append({"item": item["name"], "count": 1})
        # Same as bag_capacity = bag_capacity - item weight
        bag_capacity -= item["weight"]
    
    # Second, fill the remaining capacity with the heaviest items possible
    for item in items_available:
        while bag_capacity >= item["weight"]:
            # Find the item in the backpack and increase its count
            for packed_item in backpack:
                # Condition (if packed_item["item"] == item["name"]): This checks if the current item in the backpack is the same as the item you're trying to add.
                if packed_item["item"] == item["name"]:
                    packed_item["count"] += 1
                    break
            bag_capacity -= item["weight"]
    
    return backpack

# Test cases
print(food_backpack(27))  # Example 1
print(food_backpack(38))  # Example 2
print(food_backpack(15))  # Example 3

# Can also run entering individual amounts
# bag_capacity = 27
# bag_capacity = 38
# bag_capacity = 15


# Packed_Bag = food_backpack(bag_capacity)
# print(Packed_Bag)


# In[ ]:





# In[ ]:




