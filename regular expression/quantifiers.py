# import re
# x="a+"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x="a*"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x = "a?"
# r = "aaa abc aaaa cga"
# matcher = re.finditer(x, r)
# for match in matcher:
#      print(match.start())
#      print(match.group())
# import re
# x = "a{2}"
# r = "aaa abc aaaa cga"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x = "a{2,3}"
# r = "aaa abc aaaa cga"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x = "^a"
# r = "aaa abc aaaa cga"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
import re
x = "a$"
r = "aaa abc aaaa cga"
matcher = re.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())
