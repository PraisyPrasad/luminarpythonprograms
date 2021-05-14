# import re
# x='[abc]'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
    #print(match.group())
# import re
# x='[^abc]'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x='[a-z]'
# matcher=re.finditer(x,"abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
import re
x='[A-Z]+[a-z]'
matcher=re.finditer(x,"aBd Cp@5km")
for match in matcher:
    print(match.start())
    print(match.group())
