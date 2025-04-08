class Kata:
    def __init__(self,name):
        self.name = name
        print("Hola " + self.name)
        self.run()
    
    def input(self,message):
        if message != "Stop!":
            return message[::-1]
        else:
            return "Adios " + self.name
    
    def run(self):
        var = True
        while var:
            message = input()
            result = self.input(message)
            if result == "Adios " + self.name:
                var = False
            print(result)