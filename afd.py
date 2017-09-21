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
