import re
mail='praisyprasad123@gmai.com'
rule='^[a-z0-9]+[@][a-z]+[.][a-z]+$'
match=re.fullmatch(rule,mail)
if match is not None:
    print("valid")
else:
    print("invalid")