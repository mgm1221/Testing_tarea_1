class Kata:
    def __init__(self,name):
        self.name = name
        print("Hola " + self.name)
    
    def input(self,message):
        if message != "Stop!":
            if message == "Hola":
                return "aloH"
            elif message == "numero":
                return "oremun"
            return "omoc"
        else:
            return "Adios " + self.name