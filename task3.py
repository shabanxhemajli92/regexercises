import re
text="Berlin is a city of culture"
replace_space=re.sub("\s","-",text)
print(replace_space)