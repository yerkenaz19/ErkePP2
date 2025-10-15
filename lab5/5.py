import re
text_to_match="She put the kebab on the grill."
result=re.findall(r"\b\w*a\w*b\b", text_to_match)
print(result)