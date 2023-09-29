# class Remote():
#     pass
# class player:
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass

#     def moveTop(self):
#         pass

# remote1 = Remote()
# player1 = Player()

# if(remote1.isLeftpressed()):
#     player1.moveLeft()


class Employee:
    company = " Google"

harry = Employee()
sanket = Employee()
print(harry.company)
print(sanket.company)
Employee.company = "YouTube"
print(harry.company)
print(sanket.company)