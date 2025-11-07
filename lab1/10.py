import re
text = "Python is an amazing programming language"
result = re.sub(r"\s", "_", text)
print(result)

