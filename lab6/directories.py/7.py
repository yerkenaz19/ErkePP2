with open(r'/Users/erkenazsagynbaeva/ErkePP2/lab6/directories.py/text.txt',"r") as file1:
    with open("text_copy.txt","w") as file2:
        for line in file1:
            file2.write(line)