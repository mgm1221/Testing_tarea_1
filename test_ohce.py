from kata import Kata

def test():
    x = Kata("Martin")
    
    resultado = x.input("Hola")

    assert resultado == "aloH"

    resultado = x.input("como")

    assert resultado == "omoc"

    resultado = x.input("Stop!")

    assert resultado == "Adios Martin"

    resultado = x.input("numero")

    assert resultado == "oremun"