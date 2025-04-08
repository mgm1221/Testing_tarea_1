from kata import Kata

def test():
    x = Kata("Martin")
    resultado = x.input("stop!")
    assert resultado == "Adios Martin"