import re
text_to_match="KBTU is the best university, and historical building."
pattern=r"[ ,.]"
replace_matched_with=":"
result = re.sub(pattern, replace_matched_with, text_to_match)
print(result)