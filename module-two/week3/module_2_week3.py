import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


"""
$ grep thon /usr/share/dict/words
$ grep -i python /usr/share/dict/words # -i make grep case insensitive

$ grep l.rts /usr/share/dict/words # . is a wildcard

grep ^fruit /usr/share/dict/words #matches start od line
grep $cat /usr/share/dict/words #matches end of line

"""

result = re.search(r"aza", "plaza") #r - raw string

print(re.search(r"x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like cats and dogs.")) #finds 1st occurence

print(re.findall(r"cat|dog", "I like cats and dogs.")) #finds all occurences

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming")) # <re.Match object; span=(0, 17), match='Python Programmin'>
print(re.search(r"Py[a-z]*n", "Python Programming")) # <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"o+l+", "goldfish")) # <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly")) # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil")) # None

def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

print(re.search(r"p?each", "To each their own")) # <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "My fav fruit is peach")) # <re.Match object; span=(16, 21), match='peach'>

print(re.search(r".com", "welcome")) # <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "welcome")) # None --> \ is the escape character

print(re.search(r"\w*", "This is an example"))

print(re.search(r"^A.*a$", "Azerbaijan")) # None
print(re.search(r"^A.*a$", "Australia")) # <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))

def check_sentence(text):
  result = re.search(r"^[A-Z][A-Za-z\s]+[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True



def check_web_address(text):
  pattern = r"^[A-Za-z0-9_-]+([\-\.]{1}[A-Za-z0-9]+)*\.[A-Za-z]{2,6}$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

def check_time(text):
  pattern = r"^(?:1[0-2]|[1-9]):(?:[0-5][0-9])(?:\s?[APap][Mm])?$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

def contains_acronym(text):
  pattern = r"[(][A-Z0-9][A-Za-z]*[)]" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

def check_zip_code (text):
  result = re.search(r"\s[0-9]{5}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
