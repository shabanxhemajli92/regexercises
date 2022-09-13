import re
text="Berlin is a world city of culture, politics, media and science."
first_whitespace=re.search(r'\s',text)



print("The first white-space character is located at position: ",first_whitespace.start())#prints the location of the first whitespace