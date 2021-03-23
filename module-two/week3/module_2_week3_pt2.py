import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(f'{result[2]} {result[1]}')

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return f'{result[2]} {result[1]}'

def rearrange_name_with_initial(name):
  result = re.search(r"^([\w\.-]*), ([\w.\.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name_with_initial("Kennedy, John F.")
print(name)

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # prints 1st 5 letter word
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # ['scary', 'ghost', 'appea']

# \b matches word limits at the beginning and end of the pattern
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# {5,10} is the range
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# {5,} range with no upper limit
print(re.findall(r"\w{5,}", "I really like strawberries"))

#finds word that starts with the letter s upto 20 characters
print(re.search(r"s\w{,20}", "I really like strawberries"))

def long_words(text):
  pattern = r"[a-zA-Z]{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

re.split(r"[.?!]", "This is a sentance. With words in it." )
# ['This is a sentance', ' With words in it', '']

re.split(r"([.?!])", "This is a sentance. With words in it." )
# ['This is a sentance', '.', ' With words in it', '.', '']

re.sub(r"[\w.%+-]+@[\w.-]+", "[HIDDEN]", "This is the email for blah@blah.com")
# 'This is the email for [HIDDEN]'

re.sub(r"^([\w. +-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

def convert_phone_number(phone):
  result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'(\1) \2-\3', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

def transform_comments(line_of_code):
  result = re.sub(r"[#]+", "//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

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

def transform_record(record):
  new_record = re.sub(r",(\d{3})-", r",+1-\1-", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
