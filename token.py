##### Lista de Tokens
class Tokens:

	def reservadas(self):
		return {
			"abstract": "ABSTRACT",
			"case": "CASE",
            "class": "CLASS",
			"catch": "CATCH",
			"do": "DO",
            "def": "DEF",
			"else": "ELSE",
            "esac": "ESAC",
			"fi": "FI",
			"final": "FINAL",
            "finally": "FINALLY",
            "for": "FOR",
            "forSome": "FORSOME",
			"explicit": "IMPLICIT",
            "implicit": "IMPORT",
            "lazy": "LAZY",
            "match": "MATCH",
            "native": "NATIVE",
            "null": "NULL",
            "object": "OBJECT",
            "override": "OVERRIDE",
            "package": "PACKAGE",
            "private": "PRIVATE",
            "protected": "PROTECTED",
            "requires": "REQUIRES",
            "return": "RETURN",
            "sealed": "SEALED",
            "super": "SUPER",
            "this": "THIS",
            "throw": "THROW",
            "trait": "TRAIT",
            "try": "TRY",
            "type": "TYPE",
            "val": "VAL",
            "var": "VAR",
            "with": "WITH",
            "yield": "YIELD"
			"in": "IN",
            "inherits": "INHERITS",
            "isvoid": "ISVOID",
            "let": "LET",
            "loop": "LOOP",
            "new": "NEW",
            "of": "OF",
            "pool": "POOL",
            "self": "SELF",
            "then": "THEN",
            "while": "WHILE"

		}

	PARENTESES_ESQUERDA = 	chr(40)        # (
    PARENTESES_DIREITA = 	chr(41)        # )
    ABRE_CHAVE = 			chr(123)        # {
    FECHA_CHAVE = 			chr(125)        # }
    DOIS_PONTOS = 			chr(58)         # :
    VIRGULA = 				chr(44)         # ,
    PONTO = 				chr(46)         # .
    PONTO_VIRGULA = 		chr(59)     # ;
    ARROBA = 				chr(64)        # @
    MULTIPLICACAO = 		chr(42)      # *
    DIVISAO = 				chr(47)        # /
    ADICAO = 				chr(43)          # +
    MENOS = 				chr(45)      # -
    TIL = 					chr(126)           # ~
    MENOR_QUE = 			chr(60)            # <
    IGUAL = 				chr(61)           # =
    MAIOR_QUE_IGUAL = 		'<='        # <=
    SETA_ESQUERDA = 		'<-'     # <-
    NAO = 					'not'     # not
    FLECHA = 				'=>'      # =>


	#Regras

	#BOOLEAN - 	r"(true|false)"

	#INTEGER - 	r"\d+"
	#TYPE - 	r"[A-Z][a-zA-Z_0-9]*" ou \w
	#ID - 		r"[A-Z][a-zA-Z_0-9]*"
