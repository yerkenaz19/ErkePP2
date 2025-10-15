import re
text_to_match="The variable name must_use_underscores in_python."
result=re.findall(r"[a-z]+(?:_[a-z]+)+",text_to_match)
print(result)