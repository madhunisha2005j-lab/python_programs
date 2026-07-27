units=int(input())

if units<=100:
    bill=units*2
elif units<=200:
    bill=units*4
else:
    bill=units*6
    
print("Electricity Bill:",bill)
