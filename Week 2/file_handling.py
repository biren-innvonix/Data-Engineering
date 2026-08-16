## Reading a file
# f = open('demo.txt',"r")
# print("Content from file",f.read())
# f.close()

# # Writing a file
# content = "this is content to be write in a file"
# f = open('demo2.txt','w')
# f.write(content)
# f.close()

## Writing using with
# content = "new content"
# with open("demo2.txt", 'w') as f:
#     f.write(content)

## Appending content in file
# content = " new content"
# with open("demo2.txt", 'a') as f:
#     f.write(content)

## readLines
# with open('demo2.txt','r') as f:
#     lines = f.readlines()
#     print(lines)
# for line in lines:
#     print(line.strip())

## Reading large file
# with open('LS-5.csv', 'r') as file:
#     for line in file:
#         print(line.strip())

## Error handling in file
## Some of common Errors
## FileNotFoundError
## PermissionError
## ValueError
# try:
#     with open('abc.csv', 'r') as file:
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("File does not exists...")

## Using pathlib for file (Shorter version, Does not require with open)
# from pathlib import Path
# file_path = '/home/biren/Documents/Policy type csvs/personal/Dwelling fire csvs/PG_1.csv'
# data = Path(file_path).read_text()
# print(data)


##Copying a file
# import shutil
# shutil.copy('demo2.txt','copied.txt')