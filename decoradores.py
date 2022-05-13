def validar(func):
    def valida(x,y):
        #validação do numeros que vem da funcão soma
        if isinstance(x,int) and isinstance(y,int):
            return func(x,y)
        else:
            # mensagem de erro caso algum numero seja letras ou diferente de int
            raise ValueError, print("Voce digitou letras ao invés de numeros")
    return valida

@validar # decorador que valida a função
def soma(x,y):
    return x+y


print(soma(10,10))