import re
def camel_to_snake(text):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    return snake_case

text = "CamelCaseText"
print(camel_to_snake(text)) 