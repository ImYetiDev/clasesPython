frase1 = input("ingrese la primera frase: ")
frase2 = input("ingrese la segunda frase: ")

if len(frase1) == len(frase2):
  letras_repetidas = []

  for indice in range (len(frase1)):
      if frase1[indice] == frase2[indice]:
         letras_repetidas.append(frase1[indice])
  if len(letras_repetidas) == 0:
    print('no hay ninguna frase repetida')
  
  else:
    print('la cantidad de letras repetidas son')
    print(letras_repetidas)


else:
  print('las frases no son iguales ')