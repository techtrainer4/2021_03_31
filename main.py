# # beatles = ["john","paul","george","ringo"]
# # # Beatles = []
# # # for b in beatles:
# # #   Beatles.append(b.title())

# # #List Comprehensions
# # print([b.title() for b in beatles])
# # nums = [1,2,3,4,5]
# # nums_sq = [x**2 for x in nums]
# # print(nums_sq)

# # #While Loop
# # your_name = input("What is your name? ")
# # your_age = input("What is your age?")
# # your_age = int(your_age)
# # print(type(your_age))

# # pizza = input("Do you like pizza? Y/N? ")
# # while pizza != "Y":
# #   print("Why don't you like pizza?")
# #   pizza = input("Do you like pizza? Y/N? ")

# # foods = [] 
# # while len(foods) < 3:
# #   f = input("Please enter on of your 3 favorite foods.")
# #   foods.append(f)

# # print(foods)
# magic_num = "blue"
# money = 5
# while money > 0:
#   guess = input("What is the magic number?")
#   guess = int(guess)
#   if guess == magic_num:
#     print("You win!!!")
#     money = money + 1
#     magic_num = magic_num + 1
#   else:
#     print("That's not it!")
#     money = money - 1 #decrementing 
#     #money = money + 1 #incrementing

# if money == 0:
#   print("Game Over. Better luck next time.")

nums = [5,1,1,1,5]
repeats = [] 
for i in range(5):
  if nums[i] in nums[i + 1:]:
    repeats.append(nums[i])
print(repeats)

print(nums.count(5))

animals = ["cat","Dog"]
for a in animals:
  if a[0] == a[0].upper():
    print("%s is capitalized" % a)
  else:
    print("%s is not capitalized" % a)

MoodTracker = [] 
while len(MoodTracker) < 2:
  mood = input("How are you feeling?")
  Date = input("What is the date m/d/y?")
  Time = input("What is the time now?")
  entry = [mood, Date, Time]
  MoodTracker.append(entry)


print(MoodTracker) #not indented
print(MoodTracker[1][0])



  




  


 
