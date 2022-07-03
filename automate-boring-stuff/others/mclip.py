# mclip.py - A multi-clipboard program
import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?""",
    'avaliable': """yes! tell me."""}

if len(sys.argv)<2:
    print("Usage: python mclip.py [keyphrase] -copy phrase here")
    sys.exit()
keyphrase=sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for '{keyphrase}' copied to clipboard.")
else:
    print(f"There is no tesxt for '{keyphrase}'.")