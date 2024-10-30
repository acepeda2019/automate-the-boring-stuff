# Add all the numbers from 1-100 using a for loop
# Expected output for (0,1,2,3,4,5)
# 0+1=1
# 1+2=3
# 3+3=6
# 6+4=10
# 10+5=15  

runningTotal = 0
lowerBound = 0
upperBound = 100

for i in range(lowerBound, upperBound + 1):
    # print(f"{runningTotal} + {i} = {runningTotal + i}") #OPTIONAL: Print each iteration
    runningTotal = runningTotal + i
    
print(f"The sum of all numbers from {lowerBound} to {upperBound} is {runningTotal}!")
