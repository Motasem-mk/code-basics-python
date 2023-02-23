# for i in range(4):
#   print("# "*4)
for j in range(4):
   for i in range (4):
      print("# ",end=" ")
   print() ### must be to print new line when finishing from the nested loop 
print("^"*20)

for i in range(4):
    for j in range(4-i):
        print("*", end="  ")
    print()
print("^"*20)
for i in range(4):
    for j in range(i+1):
        print("%", end ="  ")
    print()

print("^"*20)
for i in range(4):
    for j in range(i,4):
        print("%", end ="  ")
    print()

for j in range(1,6):
   for i in range(1, 7 - j):
       print(f"{i}",end ="  ")
   print()

print(list(range(21)))
sum20 = 0
for i in list(range(21)) :
    if i % 2==0:
        sum20+=i

print(sum20)

dice_result = [5,6,4,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
n6=0
n1 = 0
j=0
for i in dice_result :
    if i == 6 :
       n6+=1
    elif i==1 :
        n1+=1


else :
    print("it doesn't appear")
print(f" 6 appeard {n6} times ")
print(f" 1 appeard {n1} times ")
print(len(dice_result))
fours = 0
le = len(dice_result)
for i in range(le):
    if dice_result[i] == 4 and dice_result[i + 1] == 4:
        fours += 1

print(f"4s came two times in a row {fours} times")

# two_6s = 0
# l = len(dice_result)
#
# for i in range(l - 1):
#  if dice_result[i] == 4 and dice_result[i + 1] == 4:
#   two_6s += 1
# print(two_6s)

print("^"* 30 )

for i in range(60):
      i+=10
      if   i == 50 :
        print("Congrats yoy have completed the challange")
        break
      elif i % 10 == 0 :
         answer = input("Are you tired ? Yes/NO ? ").lower().strip()
         if answer == "yes":
              print(f"You did {i} push ups ")
              break
         else :
                print(f"You completed {i+10} push up ")

