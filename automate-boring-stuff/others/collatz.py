#this program is exploring collatz sequence
import sys
def collatz(number):
    if number%2==0: #check number is even
            return number//2
    else:
        return 3*number+1
count=0
print("Enter number")
num=input()
try:
    n=int(num)
    while True:
        n=collatz(n)
        print(n)
        count+=1
        if n==1:
            break
    print("total steps taken=",count)
except:
    print("You must enter an integer!")
