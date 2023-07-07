NAMES = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]

def batch_badge_creator(names):
    namelist=[]
    for name in names :
        namelist.append(f"Hello, my name is {name}.")
    return namelist
    
def assign_rooms(names):
    index=1
    newlist=[]
    for name in names:
        newlist.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index+=1
    return newlist

def printer(names):
    for item in batch_badge_creator(names):
        print(item)
    for item in assign_rooms(names):
        print(item)    

print(printer(NAMES))