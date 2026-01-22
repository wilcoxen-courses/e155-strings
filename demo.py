"""
demo.py
Spring 2025 PJW

Demonstrate a range of string functions.
"""

#
#  Create a list of strings.
#
#  Notice that the last string has a comma after it even though there's no
#  subsequent string. That's allowed in Python and is very convenient for
#  lists that may need to be lengthened later.
#

stringlist = [
    "Alpha",
    "beta",
    "Gamma, delta,   epsilon",
    "día, año  , montaña ",
    "   001, 4, 0.01",
    "-123", # <- trailing comma is OK here
]

print(stringlist)

#%%
#
#  Turn it into a list of words by breaking up the strings with commas.
#  Do that by replacing the commas with spaces and then using split()
#

wordlist = []
for s in stringlist:
    words = s.replace(","," ").split()
    wordlist.extend( words )

print(wordlist)

#%%
#
#  Make a version that's all lower case
#

lower = [s.lower() for s in wordlist]
print(lower)

#%%
#
#  Make a list of the words that begin with 'a'
#

a_start = [s for s in lower if s.startswith("a")]
print(a_start)

#
#  If length of search string is fixed (e.g., always known to be 2), could get
#  the same effect with list subscripting
#

print( "abc".startswith("ab") ) # True
print( "abc"[:2] == "ab"      ) # True

#%%
#
#  Make a "tuple" of the words that begin with 'a', 'b' or '0'.
#
#  Tuples are a lot like a lists except for one important difference: they
#  can't be altered after they're created. We'll talk more about why that's
#  useful later in the semester. Tuples are created using parentheses rather
#  than square brackets.
#

starters = ("a","b","0")

ab_start = [s for s in lower if s.startswith(starters)]
print(ab_start)

#
#  Extending or revising a tuple is an error. Both of the following would fail
#

# test = starters.append("x")
# starters[0] = "A"

#%%
#
#  Make a list of the words that end with 'a'
#

a_end = [s for s in lower if s.endswith("a")]
print(a_end)

#%%
#
#  Find any words in lower containing 'ñ'.
#
#  Note that Python 3 fully supports unicode in variable names: it's OK
#  to use ñ in a variable name.
#

has_ñ = [s for s in lower if "ñ" in s]
print(has_ñ)

#%%
#
#  Use a dictionary comprehension to make a dictionary of words and their
#  lengths
#

word_lengths = { w:len(w) for w in wordlist }
print( word_lengths )

#%%
#
#  Use the dictionary to make a list of 5 letter words. This also shows how to
#  to iterate through a dictonary returning keys and values as tuples.
#

five_letter = []
for w,l in word_lengths.items():
    if l == 5:
        five_letter.append(w)
print(five_letter)

#%%
#
#  Join the words into a long string with spaces and bars between them
#

long_string = "|".join(wordlist)
print(long_string)

#%%
#
#  Find the start of a substring in a long string
#

mm_start = long_string.find("mm")
print(mm_start)

#
#  Print the string before and after the mm:
#

head = long_string[:mm_start]
tail = long_string[mm_start:]

print('first part:',head)
print('second part:',tail)

#%%
#
#  Print out words that are not just digits. Convert them to title case
#  along the way.
#
#  Note that isnumeric() does NOT handle signs or decimal points: it ONLY
#  handles strings of digits. Later in the semester we'll talk about how to
#  handle more complex cases.
#

#  Version 1 showing use of continue 

print('\nVersion 1 using continue')

numbers = []
for s in wordlist:
    
    if s.isnumeric():
        value = int(s)
        numbers.append(value)
        continue
        
    if s.isalpha():
        new_s = s.title()
        print(s,': word ->',new_s)
        continue
        
    print(s,': other')
    
total = sum(numbers)
print('\nintegers',numbers)
print('sum',total)

#%%
#
#  Since isnumeric() and isalpha() are exclusive categories (no strings are 
#  both), an alternative way to handle this particular example would be to use
#  an if/elif/else construct:
#

#  Version 2 showing use of if/elif/else

print('\nVersion 2 using if/elif/else')
    
numbers = []
for s in wordlist:
   
    if s.isnumeric():
        value = int(s) 
        numbers.append(value)
        
    elif s.isalpha():
        new_s = s.title()
        print(s,': word ->',new_s)
        
    else:
        print(s,': other')

total = sum(numbers)
print('\nintegers',numbers)
print('sum',total)
