import re
text_to_match="She decided to abbborate her notebook with glitter and stickers"
result=re.findall("ab{2,3}",text_to_match)
print(result)