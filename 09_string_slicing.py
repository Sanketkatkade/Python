# greeting = ("Good Morning,")
# name = ("Sanket!")
# # string slicing
# # print(greeting[1:8] + name[3:5])
# print(greeting + name)

# str = "SanketIsGood"
# d = str[0::2]
# print(d)

# apple = '''Hii Harry,
# How are you?
# How is going?
# '''

# for character in apple:
#     print(character)


# string methods
a = "!!Sanket!!!!!!!"
print(len(a))
print(a.rstrip("!"))
print(a.upper())
print(a.lower())
print(a.replace("Sanket", "Harry"))

blogheading = "introduction to python python"
print(blogheading.capitalize())
print(blogheading.count("python"))
print(blogheading.endswith("python"))
print(blogheading.endswith("to", 13, 15))
print(blogheading.find("to"))
print(blogheading.isalnum())
print(blogheading.isalpha())
print(blogheading.islower())
print(blogheading.isupper())
print(blogheading.isprintable())
print(blogheading.isspace())
print(blogheading.istitle())
print(blogheading.startswith("introduction"))
print(blogheading.swapcase())
print(blogheading.title())
