''' single class inheritence  
            parent class 
NOTE : A child class can inherit the parent class but a parent class cannot inherit child class
   and the 1st prefrence will be given to the child class'''

# class parent:
#     coming = True
    
#     def  cat():
#         print("I am meow")
#     def cow():
#         print("I am mauw")
        
# class child(parent):
    
#     def milk():
#         print("I am a milky boy")
#     def get():
#         print("I am a work")
#     def cow():
#         print("I am mauw")

# print(child.coming)                                   # True
# print(parent.coming)                                    # True
# child.milk()                                             # I am meow
# child.cow()                                             # I am mauw
# parent.cat()
# child.cat()
# child.get()
# parent.cow()
# parent.milk()                                           # AttributeError: type object 'parent' has no attribute 'milk'


        
''' calling with an help of an object called self parameter '''

class ironman:
    iron = True

    def software(self):
        print("I am creating a virtual software")

    def animation(self):
        print("I am creating a hologram")
        
class friday(ironman):
    jarvis = True
    
    def mission(self):
        print("We have successfully created jarvis")
        
    def cred(self):
        print("We have created the project")

    def starc(self):
        print("I am a billionare")
    
print(friday.iron)                              # True
r = ironman()                               
r.software()                                    # # I am creating a virtual software
r.animation()                                   # I am creating a hologram
w = friday()
w.cred()                                        # We have created the project
w.starc()                                       # I am a billionare
w.software()                                    # I am creating a virtual software
w.mission()                                     # We have successfully created jarvis
