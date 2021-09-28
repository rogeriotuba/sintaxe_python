def PrimeiraFuncao():
    print("Ola Mundo");

PrimeiraFuncao();

def SegundaFuncao(x):
    print(f"Ola {x} o retorno");
    print("Ola " + x + " o retorno");
    print("Ola {} o retorno".format(x));
SegundaFuncao("Rogerio");

def FuncaoImprimir():## 
    print("Digite o seu nome");
    name = input();
    print(name);
FuncaoImprimir();


def GetName(name):
    print(name);
nome= input("Digite seu nome");
GetName(nome);


