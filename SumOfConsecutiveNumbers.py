#Sum of Consecutive Numbers 
import time
end = int(input("Hello! What's the number you want to see a consecutive number of? type it here: "))
start = int(input("Do you have a specific number to start with?(default is 0): "))
sum = 0

for x in range(start,end):
 x+=1
 sum+=x

print("This is your number's consecutive number: ")
print(sum)
time.sleep(3)
print("Thank you kindly for using my code :D")