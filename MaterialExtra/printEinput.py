# Print recebe Strings como argumentos ou coisas que podem ser convertidas em strings
umFloat = 3.14
print("Numero convertido para string", umFloat)
print("Hello World")
print()
# São aceitos varias strings ou uma conjunta
print("Hello", "World")
print("Hello" + "World")
print("Podemos notar que a diferença entre uma grande string e varias quando passadas para a função é que: ")
print("Passando varios argumentos existe um espacamento automatico entre eles e passando apenas 1 a string é apresentada do jeito que foi mandada")

# O input sempre é uma String
entrada = input("Digite um numero")
print("Tipo da entrada é ", type(entrada))
print("(ERRADO)Entrada vezes 2 =",entrada*2)
#Note que a saida não foi o dobro do numero mas sim duas o que foi digitado
# Para podermos trabalhar com numericos devemos convertar antes
entrada = float(entrada)
print("Tipo da entrada é ", type(entrada))
print("Entrada vezes 2 =",entrada*2)
