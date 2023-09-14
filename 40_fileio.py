# # use open function use to read the content of the file
# f = open ('40_Sample.txt','r')
# f = open ('40_Sample.txt',) # by default the mode is r
# # data = f.read(5) # read first 5 char from the file
# # data = f.read()

# data = f.readline() # it only read the first line of the file
# print(data)

# data = f.readline() # now it will read the next line of the file
# print(data)

# f.close()


# f = open('40_another.txt','a')
# data = f.write(" and i am a coder ")
# f.close()

# f = open('40_another.txt','w')
# data = f.write(" and i am a coder ")
# f.close()

# with open('40_another.txt','r') as f:
#     a = f.read()
# if 'coder' in a:
#     print("coder is present")
# else:
#     print("coder is not present")

# with open('40_Sample.txt','w') as f:
#     a = f.write("I am sanket")
#     print(a)


with open('40_another.txt','r') as f:
    content = f.read()

content = content.replace("donkey","$%^&^%%")

with open("40_another.txt",'w') as f:
    f.write(content)