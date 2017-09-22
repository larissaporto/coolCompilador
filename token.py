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

	EPAREN = r'\('        # (
    DPAREN = r'\)'        # )
    ACHAVE = r'\{'        # {
    FCHAVE = r'\}'        # }
    DPONT = r'\:'         # :
    VIRGU = r'\,'         # ,
    PONTO = r'\.'         # .
    PONTOVIRG = r'\;'     # ;
    ARROBA = r'\@'        # @
    MULTIPLI = r'\*'      # *
    DIVISA = r'\/'        # /
    ADIC = r'\+'          # +
    MENOS = r'\-'         # -
    TIL = r'~'            # ~
    MQ = r'\<'            # <
    IG = r'\='            # =
    MQIG = r'\<\='        # <=
    SETAESQ = r'\<\-'     # <-
    NAO = r'not'          # not
    FLECHA = r'\=\>'      # =>


	#Regras

	#BOOLEAN - 	r"(true|false)"

	#INTEGER - 	r"\d+"
	#TYPE - 	r"[A-Z][a-zA-Z_0-9]*" ou \w
	#ID - 		r"[A-Z][a-zA-Z_0-9]*"
