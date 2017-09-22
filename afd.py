#Função comentada lê da string caractere a caractere

#str = "test now"

#for char in str:
#    print (char)

# Função lê do arquivo caractere a caractere

with open('README.md') as f:
  while True:
    c = f.read(1)
    if not c:
      print ("End of file")
      break
    print ("Read a character:", c)

class Estado:

    def __init__(self):
        self.handlers = {}
        self.comecaEstado = None
        self.terminaEstado = []

    def adiciona_estado(self, name, handler, fim_estado=0):
        self.handlers[name] = handler
        if fim_estado:
            self.terminaEstado.append(name)

    def colocar_comeco(self, name):
        self.comecaEstado = name

    def executa(self, cargo):
        try:
            handler  = self.handlers[self.comecaEstado]
        except:
            raise InitializationError ("deve chamar .colocar_comeco() antes de .executa()" )
            raise InitializationError ("um estado deve ser fim ao menos")

    while True:
        (novoEstado, cargo) = handler(cargo)
        if novoEstado in self.terminaEstado:
            print("chegou", novoEstado)
        else:
            handler = self.handlers[novoEstado]

class afd:

    def comeca_transicoes(caractere):
        if caractere == chr(32):  #espaço em ascii
            novoEstado = Inicial
        elif caractere.isdigit():
            novoEstado = Integ
        elif caractere.isupper():
            novoEstado = S2
        elif caractere.islower():
            novoEstado = S3
        elif caractere == chr(45): # - em ascii
            novoEstado = S4
        else caractere == chr(42): # * em ascii
            novoEstado = S5
        return (novoEstado)

    def Integ(caractere):
        if caractere.isdigit():
            novoEstado = S1
        else:
            novoEstado = Sfinal
        return (novoEstado)

    def S2(caractere):
        if caractere.isalnum():
            novoEstado = S2
        elif caractere == chr(95):
            novoEstado = S2
        else:
            novoEstado = Sfinal
        return (novoEstado)

    def S3(caractere):
        if caractere.isalnum():
            novoEstado = S3
        elif caractere == chr(95):
            novoEstado = S3
        else:
            novoEstado = Sfinal
        return (novoEstado)
