import re


# text = "open isolveit folder in code"

# match = re.findall(r'open [a-z]+|folder [a-z]+', text)
# if match is None:
#     print("error")

# result = match
# print(result)

# print(re.search(r'open [a-z]+', text))
# print("open isolveit".strip('open '))

"""Regex in action"""
with open("./dummy.txt") as f:
    text = f.readlines()

pattern = r"^[a-zA-Z_][\w]+[\S]" # same as below pattern
# pattern = r"^[a-zA-Z_][\w]*$"
[print(re.search(pattern, line.strip('\n')), re.ASCII) for line in text]
# print(re.search(pattern, "_name_of_user2"))
# print(re.search(pattern, "3_name_of_user"))
# print(re.search(pattern, "name2_of_user"))


def check_web_address(text):
  pattern = r"^[\w\.\+-]+\.[a-zA-Z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


def check_time(text):
  pattern = r"^\d{1,2}:[0-5][0-9] ?[a|p]m"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


def contains_acronym(text):
  pattern = r"\([A-Z0-9][a-zA-Z0-9]+\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

def check_zip_code (text):
  result = re.search(r" [0-9]{5}[-0-9]*", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

def transform_record(record):
  new_record = re.sub(r"([\d-]+)", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

def multi_vowel_words(text):
  pattern = r"\w*[aeiou]{3,}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

def transform_comments(line_of_code):
  result = re.sub(r"(#+)", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300wgttw