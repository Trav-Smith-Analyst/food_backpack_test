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
    # backpack = [] represents an empty list that will store the items packed.
    backpack = []
    for item in items_available:
        backpack.append({"item": item["name"], "count": 1})
        # adds 1 of each item to the backpack
        # Same as bag_capacity = bag_capacity - item weight
        bag_capacity -= item["weight"]
    
    # Second, fill the remaining capacity with the heaviest items possible
    for item in items_available:
        while bag_capacity >= item["weight"]:
            # Continues to add the item to the backpack as long as there is enough capacity left in the backpack.
            # Find the item in the backpack and increase its count
            for packed_item in backpack:
                if packed_item["item"] == item["name"]:
                # Condition checks if the current item in the backpack is the same as the item you're trying to add.
                    packed_item["count"] += 1
                    break
            # Reduces the bag_capacity by the weight of the item after adding it.
            bag_capacity -= item["weight"]
    
    return backpack

# Test cases
print(food_backpack(27))  # Input Bag Capacity: 27
print(food_backpack(38))  # Input Bag Capacity: 38
print(food_backpack(15))  # Input Bag Capacity: 15

# Can also run entering individual amounts
# bag_capacity = 27
# bag_capacity = 38
# bag_capacity = 15


# Packed_Bag = food_backpack(bag_capacity)
# print(Packed_Bag)

