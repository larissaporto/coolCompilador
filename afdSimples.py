"""Classe do Autômato Finito Determinístico"""



class AfdSimples(object):
    """docstring forAfdSimples."""
    def __init__(self, estados=[]):
        self._estados = estados
        self.estadoAtual = None

    def inicio(self, inicioEstado = None):
#Início do Autômato Finito Determinístico
        if not inicioEstado or not (inicioEstado in [x[0] for x in self._estados]):
            raise ValueError ("Não é um estado inicial válido")
        self.estadoAtual = inicioEstado

    def parada(self):
#Para o AFD
        self.estadoAtual = None

    def adicionaTransicao(self, deEstado, paraEstado, condicao, callback = None):
#Adiciona transição para a lista
        if not self.estadoAtual:
            raise ValueError ("Máquina já começou - não pode adicionar novas transições")
        self._estados.append( (deEstado, paraEstado, condicao, callback))

    def evento(self, valor):
#gatilho para transição
        if not self.estadoAtual:
            raise ValueError("Máquina não começou - não processa evento")

        self.proxEstados = [ x for x in self._estados \
                            if x[0] == self.estadoAtual and (x[2] == True \
                            or (callable(x[2]) and x[2](valor)))]

        if not self.proxEstados:
            raise ValueError ("Sem transições definidas do estado {0} com valor '{1}'".format(self.estadoAtual, valor))

#        elif len(self.proxEstados) > 1:
#            raise ValueError ("Transições ambíguas do estado {0} com valor '{1}' -> Novos estados definidos {2}".format(self.estadoAtual, valor, [x[0] for x in self.proxEstados]))
        else:
            if len(self.proxEstados[0]) == 4:
                atual, next, condicao, callback = self.proxEstados[0]
            else:
                atual, next, condicao = self.proxEstados[0]
                callback = None

            self.estadoAtual, mudou = (next, True) \
                if self.estadoAtual != next else (next, False)
#volta
            if callable(callback):
                callback(self, valor)

            return self.estadoAtual, mudou

    def EstadoAtual(self):
        return self.estadoAtual

#guardar o objeto para cada token
class token(object):
    """docstring for token."""
    def __init__(self, tipo):
        self.tokenTipo = tipo
        self.tokenTexto = ""

    def adicionaChar(self, char):
        self.tokenTexto += char

#    def tokenCompara(self):
#tem que implementar com as palavras reservardas e . , = + etc...
#        return "{0}<{1}>".format(self.tokenTipo, self.tokenTexto)

#para poder refazer os passos - tipo o desafio das 8 rainhas xadrez
class tokenLista(object):
    """docstring for tokenLista."""
    def __init__(self):
        self.tokenLista = []
        self.tokenAtual = None

    def inicioToken(self, maquina, valor):
        self.tokenAtual = token(maquina.EstadoAtual())
        self.tokenAtual.adicionaChar(valor)

    def adicionaChar(self, maquina, valor):
        self.tokenAtual.adicionaChar(valor)

    def fimToken(self, maquina, valor):
        self.tokenLista.append(self.tokenAtual)
        self.tokenAtual = None

if __name__ == "__main__":

    t = tokenLista()

    maq = AfdSimples ( [ ("Inicio", "Inicio", lambda x: x == chr(32) ),
                         ("Inicio", "Digito", lambda x: chr(47) < x < chr(58), t.inicioToken ),
                         ("Digito", "Digito", lambda x: chr(47) < x < chr(58), t.adicionaChar ),
                         ("Digito", "Digito1", lambda x: x == chr(46), t.adicionaChar ),
                         ("Digito1", "Digito1", lambda x: chr(47) < x < chr(58), t.adicionaChar ),
                         ("Digito1", "Inicio", lambda x: x < chr(48) or x > chr(57), t.fimToken ),
                         ("Digito", "Inicio", lambda x: x < chr(48) or x > chr(57), t.fimToken ),
                         ("Inicio", "Identifier", lambda x: chr(96) < x < chr(123), t.inicioToken ),
                         ("Identifier", "Identifier", lambda x: chr(96) < x < chr(123) or \
                          chr(64) < x < chr(91) or x == chr(95), t.adicionaChar ),
                         ("Identifier", "Inicio", lambda x: x < chr(97) or x > chr(122) or \
                          x < chr(65) or x > chr(90) or x != chr(95), t.fimToken ),
                         ("Inicio", "Type", lambda x: chr(64) < x < chr(91), t.inicioToken ),
                         ("Type", "Type", lambda x: chr(96) < x < chr(123) or \
                          chr(64) < x < chr(91) or x == chr(95), t.adicionaChar ),
                         ("Type", "Type", lambda x: x < chr(97) or x > chr(122) or \
                          x < chr(65) or x > chr(90) or x != chr(95), t.fimToken )
                         #falta comentário com as strings
                        ]

                        )
    maq.inicio("Inicio")

    with open('README.md') as a:
      while True:
        c = a.read(1)
        if not c:
          print ("End of file")
          break
        print ("Read a character:", c)
        ret = maq.evento(c)

    ret = maq.evento("")
    print (t.tokenLista)
