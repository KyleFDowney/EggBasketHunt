
# coding: utf-8

# In[1]:

class room2(EggBasketHunt):
    getItems(2)
    def __init__(self)
    movement = input("Type S to exit Room 2")
    if movement == "S":
        room8
    else: 
        print ("You can't go that way")
    
        
    
    


# In[ ]:

class room8(EggBasketHunt):
    getItems(8)
    def __init__(self)
    movement = input("Type N to enter Room 2, S to enter Room 5, E to move East, or W to move West")
    if movement == "N":
        room2
    if movement == "S":
        room5
    if movement == "E":
        room9
    if movement == "W":
        room7
    else:
        print ("You can't go that way")


# In[ ]:

class room5(EggBasketHunt):
    getItems(5)
    def __init__(self)
    movement = input("Type N to exit room 5")
    if movement == "N":
        room8
    else:
        print ("You can't go that way")

