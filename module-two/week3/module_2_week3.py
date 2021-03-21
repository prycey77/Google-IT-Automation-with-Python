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