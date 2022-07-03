import re

print("Enter your input:")
user_input=input()

PhoneRegex=re.compile(r"\d{3}-\d{3}-\d{4}")
co=PhoneRegex.search(user_input)
print("Phone Number :",co.group())


