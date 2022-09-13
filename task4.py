import re
text="Berlin is a city of culture."
pattern=r'.n'
search_pattern=re.search(pattern,text)
print(search_pattern)