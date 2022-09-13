#task5
import re
text="Berlin is a city of culture."
pattern=r'^B\w+'
search_pattern=re.search(pattern,text)
print(search_pattern)