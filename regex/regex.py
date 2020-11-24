import re


"""Simple Matching"""

text = "pythonista"
result = re.search(r'is', text)
# print(result)

# Using ^ which means begins with
text = "regex"
result = re.search(r'^r', text)
# print(result)

# Using . (wildcard) which means any character
text = "penguin"
result = re.search(r'p.ng', text)
# print(result)

# Using $ which means ends with
text = "loging"
result = re.search(r'g.ng$', text)
# print('$',result)

# Using re.IGNORECASE which means match with case insensitive
text = "pPanda"
result = re.search(r'P.n', text, re.IGNORECASE)
# print(result)


"""Wildcard Characters and Classes"""

# Using character classes - []
# print(re.search(r'[Pp]ython', 'pythonista'))
text = "The success of the brand is imporTant"
print(re.search(r'[a-z]and', text))
print(re.search(r"impor[a-zA-z0-9]ant", text))    # combine many ranges
print(re.search(r'[^a-zA-z]', text))    # match any character not in the range
print(re.search(r'[^a-z]brand', text))  # matches ' brand'
print(re.search(r'[^a-z ]brand', text))  # doesn't match spaces

# Using the pipe symbol (|) which means or 
text = "I like yam"
text2 = "I like rice"
print(re.search(r"rice|yam", text2))

# Using re.findall to match all possible occurences
text = "The success of the brand is important to the band"
print(re.findall(r'[a-z]and', text))
print(re.findall(r'band|rand', text))  # Same as above


"""Repitition Qualifiers"""
# Match Python from string
print(re.search(r"Py.*n", "Python Programming"))    # Python Programmin -[Greedy Matching]
# Do this instead of above
print(re.search(r"Py[a-z]*n", "Python Programming"))
# Using the + symbol which means one or more occurences
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+d+", "goldfish"))   # None - Bcus l is between o & d
# Using the ? symbol which means zero or one occurence
print(re.search(r"o?range", "You know the range"))
print(re.search(r"o?range", "I like orange"))


"""Escaping Characters"""
# Using the \ symbol which is for escaping charatcers
print(re.search(r"\.com", "mydomain.com"))
# Special Sequences
# Using \w for matching any alphanumeric character
print(re.search(r'\w*', "This is an example"))

# Advance Concepts
"""Capturing Groups"""
result = re.search(r"^(\w*), (\w*)$", "Duodu, Randy")
print(result)
print(result.groups())  # returns a tuple with the number of elements in the tuple based on the number of groups in the pattern
print(f"{result[2]} {result[1]} is simplified version of {result[0]}")

"""More on Repetition Qualifiers"""
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

"""Extracting a ProcessID Using regexes in Python"""
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
pattern = r"\[(\d+)\]"
result = re.search(pattern, log)
print(result[1])

"""Splitting and Replacing"""
# Using re.split(pattern, string) which splits string based on the pattern and returns a list
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

# Using re.sub(pattern, repl, string)
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Duodu, Randy"))