from kata import Kata

def test():
    x = Kata("Martin")
    
    resultado = x.input("Stop!")

    assert resultado == "Adios Martin"