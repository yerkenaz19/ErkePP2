import re
def snakeToCamel(text):
    words = re.split(r'_', text)
    camelCase = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camelCase
snake_case_string = "hello_world_example"
camel_case_string = snakeToCamel(snake_case_string)
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)