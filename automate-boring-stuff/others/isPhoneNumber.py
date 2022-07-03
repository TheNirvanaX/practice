def isPhoneNumber(number):
    if len(number)>12:
        return False
    num=number.split("-")
    if len(num)!=3 or len(num[0])!=3 or len(num[2])!=4:
        return False
    for i in num:
        if not i.isdecimal():
            return False
    return True
'''
print("enter your number:")
number=input()
print(isPhoneNumber(number))
'''
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
