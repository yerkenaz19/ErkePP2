import re
def camel(text):
    snake_case=re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    return snake_case.lower()
text="CamelCaseText"
print(camel(text))
