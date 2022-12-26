dollars = input("How much was the meal? ")
percent = input("What percentage would you like to tip? ")
dollars1=""
percent1=""
for i in range(1,len(dollars)):
      dollars1=dollars1+dollars[i]
dollars1=float(dollars1)

for i in range(0,len(percent)-1):
      percent1=percent1+percent[i]
percent1=float(percent1)

print(f"Leave ${float(dollars1*percent1)/100:.2f}")