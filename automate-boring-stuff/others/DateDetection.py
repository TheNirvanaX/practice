# Date Detection - This prohram detects Date DD/MM/YYYY format
import re
import pyperclip
import ValidDate as vd

# get input from clip board
text = str(pyperclip.paste())

# create Date Regex object Date format: dd/mm/yyyy
DateRegex1 = re.compile(r'''(
    ([0-3]?\d)               # day
    (/|\.|-)               # seperator
    ([0-1]?\d)               # month
    (/|\.|-)               # seperator
    ([1-2]\d\d\d)            # year
    )''', re.VERBOSE)

# find date
Date = DateRegex1.findall(text)
Dates = []

for group in Date:
    day = group[1]
    if len(day) == 1:
        day = "0"+day     # add leading zero to single digit day

    month = group[3]
    if len(month) == 1:
        month = "0"+month  # add leading zero to single digit month

    year = group[5]

    if vd.isValidDate(day, month, year):
        date = str(day+"/"+month+"/"+year)
        if date not in Dates:
            Dates.append(date)


# copy to clip board
if len(Dates) < 1:
    print("No Dates Found!")
else:
    Dates = "\n".join(Dates)
    print("Dates Found:")
    print(Dates)
    pyperclip.copy(Dates)
