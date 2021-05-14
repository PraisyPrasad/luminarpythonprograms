import re
x='[A-Z]+[a-z]+$'
matcher=re.finditer(x,"AaBbGg")
for match in matcher:
    print(match.start())
    print(match.group())