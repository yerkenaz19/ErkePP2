import re
text_to_match="AtyrauILoveYou MissYou"
result = re.sub(r"(?=[A-Z])", " ", text_to_match).strip()
print(result)