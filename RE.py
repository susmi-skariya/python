import re

# re.search(pattern, string) #

# text = "Hello world"
# print(re.search(r"world", text))

# re.match(pattern, string) #

# text = "Hello world"
# print(re.match(r"Hello", text)) 

# re.findall(pattern, string) #

# text = "I have 2 apples and 5 oranges."
# print(re.findall(r"\d", text))

# text1 = "I have 45 apples and 55 oranges"
# print(re.findall(r"\d+",text1))

# re.finditer(pattern, string) #

# text = "I have 5 apples and 6 oranges."
# for match in re.finditer(r"\d+", text):
#     print(match.group(), "at", match.start())

# re.sub(pattern, repl, string) #

# text = "Hello 123, welcome 456!"
# print(re.sub(r"\d+", "number", text))
# print(re.sub(r"\d+", "Aami", text))

# re.split(pattern, string) #

# text = "apple, orange; banana, grape"
# print(re.split(r"[;,]", text)) 

# Grouping & Capturing #

# text="Aami: 25, susmi: 18, Ajay: 26"
# print(re.findall(r"(\w+): (\d+)",text))

# Compiling Regex #

# pattern = re.compile(r"\d+")
# text = "123 apples and 456 oranges"
# text1 = "345 biscuits and 567 cakes"
# text3 = "333 parrots and 444 crows"
# print(pattern.findall(text))
# print(pattern.findall(text1))
# print(pattern.findall(text3))

# **** Meta Charecters **** #



## Regex Flags ##

# re.IGNORECASE (or re.I ) : Makes the pattern case-insensitive #

# text ="HELLO world"
# print(re.search(r"hello", text, re.I))

# re.MULTILINE (or re.M ) #

# text ='''first line
# second line
# third lines'''

## finding the string starting with s ##

# print(re.findall(r"^s\w+", text, re.MULTILINE)) 

# finding the string ending with e #

# print(re.findall(r"\w+s$",text,re.MULTILINE))

## re.DOTALL (or re.S ) ##

# text =  "Hello\nWorld"

# print(re.search(r"Hello.*World", text))

## with re.DOTALL ##

# print(re.search(r"Hello.*World", text, re.DOTALL))



#*** Real-Life Uses of Regular Expressions ***#

# Validation (Checking Input) : Email addresses, phone numbers, PIN codes, passwords, etc. #

# email = "user@example.com"
# if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
#  print("Valid email")
# else:
#  print("Invalid email")

# Data Cleaning : Remove unwanted characters, spaces, or symbols. #

# text = "Price: $123.45"
# print(re.sub(r"[^0-9.]", "", text))

# Text Extraction :Extracting dates, phone numbers, hashtags, mentions, etc.#

# tweet = "Excited for #Python3 and following @openai!"
# print(re.findall(r"#\w+", tweet))
# print(re.findall(r"@\w+", tweet))

# Search & Replace : Replace phone numbers with XXX , mask credit cards, etc #

# text = "Card: 1234-5678-9012-3456"
# print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", text))
# print(re.sub(r"\d{4}-\d{4}-\d{4}-", "****-****-****-", text))


