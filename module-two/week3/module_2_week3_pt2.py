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

re.split(r"[.?!]", "The is a sentance with words in it." )