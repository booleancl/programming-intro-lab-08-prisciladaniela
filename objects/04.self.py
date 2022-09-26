# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 

class Student: 
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills

    def say_name(self):
        print("Mi nombre es", self.name,",mi puesto de trabajo es",self.position,"y mis habilidades son",self.skills)
        
alice = Student ("Alice","Fullstack Developer","Python,Git,HTML,CSS,Javascript")
bob = Student("Bob","chef","responsable y compañerismo" )



print(type(Student))

alice.say_name()
bob.say_name()

  


