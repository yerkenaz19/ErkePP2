import os
path = os.getcwd()
for i in range(65, 91):  
    letter = chr(i)               
    file_name = f"{letter}.txt"
    file_path = os.path.join(path, file_name)

    with open(file_path, "w") as file:
        file.write(f"This is {file_name}\n")

    print(f"Created: {file_path}")


