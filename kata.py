class Kata:
    def __init__(self,name):
        self.name = name
        print("Hola " + self.name)
    
    def input(self,message):
        if message == "Hola":
            return "aloH"
        elif message == "como":
            return "omoc"
        else:
            return "Adios " + self.name