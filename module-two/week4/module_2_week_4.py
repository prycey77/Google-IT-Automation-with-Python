import subprocess

subprocess.run(["date"])
"""
Thu 25 Mar 2021 10:50:59 GMT
CompletedProcess(args=['date'], returncode=0)
"""
subprocess.run(["sleep", '3'])

result = subprocess.run(["ls",  "this_file_does_not_exist"])
print(result.returncode)


result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n' 
print(result.stdout.decode().split())
# ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode) #1
print(result.stdout) #b''
print(result.stderr.decode()) #rm: does_not_exist: No such file or directory

