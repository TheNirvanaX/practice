#this program exctractors emails and phone numbers from copied text.

import re
import pyperclip

#create regex object for email
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''',re.VERBOSE)

# create regex object for phone number
PhoneNumberRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # Area code
    (\.|-|\s)?                       # hyphen or dot or space
    \d{3}                            # first 3 digit
    (\.|-|\s)                        # hyphen or dot or space
    \d{4}                            # last 4 number
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension  
    )''',re.VERBOSE)


# capture/patse input from clipboard
text=pyperclip.paste()

list=[]
# find phone number
result=PhoneNumberRegex.findall(text)
for tup in result:
    
    number=tup[0].split(".")        # Replace dot by hyphen
    number="-".join(number)

    if number in list:              # check for repeated number
        continue
    list.append(number)

#find email
resultemail=emailRegex.findall(text)
for tup in resultemail:
    email=tup[0]
    if email in list:               # check for repeated email
        continue
    list.append(email)

# join list into string
if len(list)<1:
    print(new_text="No email and Phone number found!")
else:
    new_text="\n".join(list)
    # copy results into clipboard
    pyperclip.copy(new_text)
    print("copied to clipboard:")
    print(new_text)
