'''
    weekly wages : hr wages $ 12 and for overtime 1.5 times of hourly wages 

'''
print("Enter input how many hr you work on each day")
Weekday=['Monday','Tuesday','Wednsday','Thusday','Friday','Saturday','Sunday']
Hours=[]

for i in Weekday:
   x= int(input(f"Enter Hours work on {i} :"))
   Hours.append(x)

wages= int(input("Enter your Hr wages : "))
print('days you worked : ' ,Weekday)  
print('HR work this week : ' ,Hours)
print('Yout HR rate : ' , wages)

total = 0
for hr in Hours:
   total = total+hr
print(f"Total Hours week this week : {total}")

paycheck = 0
if total <= 40 :
   paycheck = total *wages
elif total > 40:
   paycheck = 40* wages
   paycheck = paycheck + ((total-40)*(1.5*wages))

print(f"Your Paycheck is : {paycheck}")



'''
Hours = input("Enter Hr you worked : ")
print(type(Hours))
print(Hours)

wek_hr = [int(x) for x in Hours.split()]
print(wek_hr)'''