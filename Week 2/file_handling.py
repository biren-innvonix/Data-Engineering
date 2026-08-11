## Reading a file

# f = open('demo.txt',"r")
# print("Content from file",f.read())
# f.close()

## Writing a file

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
