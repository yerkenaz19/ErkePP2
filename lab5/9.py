import re
text = "WeLoveKazakhstan"
result = re.sub(r"(?<!^)(?=[A-Z])", " ", text)
print(result)