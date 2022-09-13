#task6
import re
text="The rain in Spain"
ai_count=re.findall("ai",text)
print(len(ai_count))