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
        self.tipo = ""

    def adicionaChar(self, char):
        self.tokenTexto += char

    def determinaTipo(self):
        reservadas = ('abstract', 'case', 'class', 'catch', 'do', 'def', 'else', \
                        'esac', 'fi', 'final', 'finally', 'for', 'forSome', 'explicit', \
                        'implicit', 'lazy', 'match', 'native', 'null', 'object', 'override', \
                        'package', 'private', 'protected', 'requires', 'return', 'sealed', \
                        'super', 'this', 'throw', 'trait', 'try', 'type', 'val', 'var', 'with' \
                        'yield', 'in', 'inherits', 'isvoid', 'let', 'loop', 'new', 'of', \
                        'pool', 'self', 'then', 'while')

        if self.tokenTexto in reservadas:
            self.tipo = 'reservada'
        elif self.tokenTexto == '<=':
            self.tipo = 'MAIOR_QUE_IGUAL'
        elif self.tokenTexto == '<-':
            self.tipo = 'SETA_ESQUERDA'
        elif self.tokenTexto == 'not':
            self.tipo = 'NEGACAO'
        elif self.tokenTexto == '=>':
            self.tipo = 'FLECHA'
        else:
            tamanho = len(self.tokenTexto)
            if self.tokenTexto[0:1] == '--' or tamanho > 0 and self.tokenTexto[0] == '*' and self.tokenTexto[tamanho-1] == '*':
                self.tipo = 'COMENTARIO'
            else:
                self.tipo = 'Identifier'

        return self.tipo

    def __repr__(self):
        return "{0}<{1}>".format(self.tokenTipo, self.tokenTexto)



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
        a = token(maquina.EstadoAtual())
        b = a.determinaTipo()

        self.tokenLista.append(self.tokenAtual)
        self.tokenAtual = None


if __name__ == "__main__":

    t = tokenLista()

    maq = AfdSimples (
        [
            ("Inicio", "Inicio", lambda x: ord(x) == 32 or ord(x) == 10),
            ("Inicio", "Digito", lambda x: 47 < ord(x) < 58, t.inicioToken ),
            ("Digito", "Digito", lambda x: 47 < ord(x) < 58, t.adicionaChar ),
            ("Digito", "Digito1", lambda x: ord(x) == 46, t.adicionaChar ),
            ("Digito1", "Digito1", lambda x: 47 < ord(x) < 58, t.adicionaChar ),
            ("Digito1", "Inicio", lambda x: ord(x) < 48 or ord(x) > 57, t.fimToken ),
            ("Digito", "Inicio", lambda x: ord(x) < 48 or ord(x) > 57, t.fimToken ),
            ("Inicio", "Identifier", lambda x: 96 < ord(x) < 123, t.inicioToken ),
            ("Identifier", "Identifier", lambda x: 96 < ord(x) < 123 or \
                64 < ord(x) < 91 or ord(x) == 95, t.adicionaChar ),
            ("Identifier", "Inicio", lambda x: ord(x) < 97 or ord(x) > 122 or \
                ord(x) < 65 or ord(x) > 90 or ord(x) != 95, t.fimToken ),
            ("Inicio", "Type", lambda x: 64 < ord(x) < 91, t.inicioToken ),
            ("Type", "Type", lambda x: 96 < ord(x) < 123 or \
                64 < ord(x) < 91 or ord(x) == 95, t.adicionaChar ),
            ("Type", "Type1", lambda x: 32 < ord(x) < 97 or ord(x) > 122 or \
                32 < ord(x) < 65 or ord(x) > 90 or ord(x) != 95 and ord(x) != 32 and ord(x) != 10, t.adicionaChar ),
            ("Type1", "Type1", lambda x: 32 < ord(x) < 97 or ord(x) > 122 or \
                32 < ord(x) < 65 or ord(x) > 90 or ord(x) != 95 and ord(x) != 32 and ord(x) != 10, t.adicionaChar ),
            ("Type", "Inicio", lambda x: ord(x) == 32 or ord(x) == 10 , t.fimToken),
            ("Type1", "Inicio", lambda x: ord(x) == 32 or ord(x) == 10 , t.fimToken),
            ("Inicio", "Comentario", lambda x: ord(x) == 45, t.inicioToken),
            ("Comentario", "Comentario1", lambda x: ord(x) == 45, t.adicionaChar),
            ("Comentario1", "Comentario1", lambda x: ord(x) != 10, t.adicionaChar),
            ("Comentario1", "Inicio", lambda x: ord(x) == 10, t.fimToken),
            ("Inicio", "Comentario2", lambda x: ord(x) == 42, t.inicioToken),
            ("Comentario2", "Comentario2", lambda x: ord(x) != 42, t.adicionaChar),
            ("Comentario2", "Comentario3", lambda x: ord(x) == 42, t.adicionaChar),
            ("Comentario3", "Comentario2", lambda x: ord(x) != 10, t.adicionaChar),
            ("Comentario3", "Inicio", lambda x: ord(x) == 10, t.fimToken),
            ("Inicio", "PARENTESES_ESQUERDA", lambda x: ord(x) == 40, t.inicioToken ),
            ("PARENTESES_ESQUERDA", "Inicio", True, t.fimToken ),
            ("Inicio", "PARENTESES_DIREITA", lambda x: ord(x) == 41, t.inicioToken ),
            ("PARENTESES_DIREITA", "Inicio", True, t.fimToken ),
            ("Inicio", "ABRE_CHAVE", lambda x: ord(x) == 123, t.inicioToken ),
            ("ABRE_CHAVE", "Inicio", True, t.fimToken ),
            ("Inicio", "FECHA_CHAVE", lambda x: ord(x) == 125, t.inicioToken ),
            ("FECHA_CHAVE", "Inicio", True, t.fimToken ),
            ("Inicio", "DOIS_PONTOS", lambda x: ord(x) == 58, t.inicioToken ),
            ("DOIS_PONTOS", "Inicio", True, t.fimToken ),
            ("Inicio", "VIRGULA", lambda x: ord(x) == 44, t.inicioToken ),
            ("VIRGULA", "Inicio", True, t.fimToken ),
            ("Inicio", "PONTO", lambda x: ord(x) == 46, t.inicioToken ),
            ("PONTO", "Inicio", True, t.fimToken ),
            ("Inicio", "PONTO_VIRGULA", lambda x: ord(x) == 59, t.inicioToken ),
            ("PONTO_VIRGULA", "Inicio", True, t.fimToken ),
            ("Inicio", "ARROBA", lambda x: ord(x) == 64, t.inicioToken ),
            ("ARROBA", "Inicio", True, t.fimToken ),
            ("Inicio", "MULTIPLICACAO", lambda x: ord(x) == 42, t.inicioToken ),
            ("MULTIPLICACAO", "Inicio", True, t.fimToken ),
            ("Inicio", "DIVISAO", lambda x: ord(x) == 47, t.inicioToken ),
            ("DIVISAO", "Inicio", True, t.fimToken ),
            ("Inicio", "ADICAO", lambda x: ord(x) == 43, t.inicioToken ),
            ("ADICAO", "Inicio", True, t.fimToken ),
            ("Inicio", "MENOS", lambda x: ord(x) == 45, t.inicioToken ),
            ("MENOS", "Inicio", True, t.fimToken ),
            ("Inicio", "TIL", lambda x: ord(x) == 126, t.inicioToken ),
            ("TIL", "Inicio", True, t.fimToken ),
            ("Inicio", "MENOR_QUE", lambda x: ord(x) == 60, t.inicioToken ),
            ("MENOR_QUE", "Inicio", True, t.fimToken ),
            ("Inicio", "IGUAL", lambda x: ord(x) == 61, t.inicioToken ),
            ("IGUAL", "Inicio", True, t.fimToken ),
            ("Inicio", "EOF", lambda x: x == chr(3)),
            ("EOF", "Inicio", True)
        ]

    )
    maq.inicio("Inicio")

    with open('ReadMe2.md') as a:
        while True:
            c = a.read(1)
            if not c:
                print ("End of file")
                b = chr(3)
                ret = maq.evento(b)
                break
            print ("Read a character:", c)

            ret = maq.evento(c)
#        if ret[0] != "Start" or (ret[0] == "Start" and ret[1] == False):
#            c = a.read(1)

#       ret = maq.evento("")
    print (t.tokenLista, file = open('saida.txt', 'a'))
    print (t.tokenLista)
