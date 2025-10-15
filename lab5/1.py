import re
text_to_match=" The rabbit swiftly hopped across the grassy field."
pattern="ab*"
result=re.findall(pattern, text_to_match)
print(result)
