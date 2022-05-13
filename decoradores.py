def validar(func):
    def valida(x,y):
        if isinstance(x,int) and isinstance(y,int):
            return func(x,y)
        else:
            raise ValueError, print("Voce digitou letras ao invés de numeros")
    return valida

@validar # decorador que valida a função
def soma(x,y):
    return x+y


print(soma(10,10))