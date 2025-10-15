import re
text_to_match="My PP2 teacher is miss Akbota"
results=re.finditer(r"[A-Z]+[a-z]+",text_to_match)
print(results)
for result in results:
    print(result)