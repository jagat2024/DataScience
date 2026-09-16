# p = open(r"C:\Users\Home\Desktop\my prespective.txt", "r")
# print(p.read())
# p.close()

# with open("name.txt", "w") as f:
#     f.write("jagat prasanna shaw\n")

# with open("name.txt", "a") as f:
#     f.write("Age: 22\n")
#     f.write("Gender: Male")

# with open("name.txt", "r") as f:
#     print(f.readlines())
count=0
# with open("name.txt", "r") as f:
#     text = f.read()
# f.close()

# words = text.split()
# print("The number of words in the file is:", len(words))
with open("name.txt", "r") as f:
    while(f.readline()!=""):
        count=count+1
print("the no of lines is" , count)
with open("copy_file.txt","w+")as c:
    with open("name.txt", "r") as f:
        c.write(f.read())
with open("copy_file.txt","r+")as c:
    print(c.read())
with open("name.txt", "r") as f:
    text=f.read();
words= text[::-1]
for word in words:
    print(word,end="")