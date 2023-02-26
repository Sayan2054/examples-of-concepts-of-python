#Example of file handling

# main.py

# Writing to a file
with open("myfile.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a Python file.\n")
    f.write("We're learning file handling today.\n")

# Reading from a file
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)

'''output:-
Hello, World!
This is a Python file.
We're learning file handling today.
'''
