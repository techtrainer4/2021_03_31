print(4 == 4) #True Boolean True False
print(2 * 2 == 2 + 2 == 3 + 1)
print("5" != 5)
print(5 > 4)
print(10 < 3)

age = 12
#G,PG,PG13,R
rating = "PG13"

def Movie_Permission(age,rating):
  can = "You can watch this movie!"
  cant = "You cannot watch this movie!"
  parent = "You might need a parent to watch this."
  if age >= 18 and rating == "R":
    print(can)
  elif age >= 13 and rating == "PG13":
    print(can)
  elif age >= 5 and rating == "PG":
    print(parent)
  elif rating == "G":
    print(can)
  else: 
    print(cant)
  

Movie_Permission(14,"PG13")


rain = False
cold = False
wind = False
warm_clothes = False 

def Can_I_Go_Out(rain,cold,wind,warm_clothes):
  can = "You can go out to eat."
  cant = "You can't go out to eat."
  if cold and warm_clothes:
    print(can)
  elif wind and warm_clothes: 
    print(can)
  elif not rain and not cold and not wind:
    print(can)
  else:
    print(cant)

Can_I_Go_Out(False,True,True,False)






  


 
