# A declaração de varaveis é simples em python
# Os tipos de variaveis em python são:
umInteiro = 1          # integer(inteiro)
umFloat = 2.143       # Float/Double(decimal)
umaString = "Python String"  # String(Sequencia de caracteres)
umBoolean = True  # Boolean(logico)
x = "Nome de variavel não recomendado"
print("Variavel umInteiro:", umInteiro)
print("Variavel umFloat:", umFloat)
print("Variavel umaString:", umaString)
print("Variavel x:", x)
print("Variavel umBoolean", umBoolean)
# Podemos fazer operações matematicas com variaveis
# Utilizamos + para soma, - para subtrair
#  * para multiplicar, / para dividir e % para o resto da divisão
print("Inteiro mais 1 =", umInteiro + 1)
print("Um float mais 0.25 =", umFloat + 0.25)
# Variaveis podem mudar o seu valor conforme a nossa necessidade
# Nessa parte do codigo estamos utilizando o valor anterior da variavel umInteiro multiplicando por 2 e depois guardamos o valor na propia variavel
umInteiro = umInteiro * 2
print("Um inteiro agora é:", umInteiro)
# Para fazer contas mais complexas podemos utilizar parenteses para definir a ordem das operações
resultadoConta = (umInteiro+umInteiro)*3
print("Conta com parentese =", resultadoConta)
resultadoConta = umInteiro+umInteiro*3
print("Conta sem parentese =", resultadoConta)
# Podemos somar um inteiro e double
print("Somando inteiro com float =", (umInteiro + umFloat))
# Variaveis são especialmente uteis para guardar entradas do usuario
umFloat = input("Digite um valor!")
print("Variavel umFloat: ", umFloat)
# O input retorna SEMPRE uma string, então para trabalhar com numeros devemos converter(Informações adicionais podem ser encontradas no Material Extra)
umFloat = float(umFloat)
# ou umInteiro=int(umInteiro) para converter algo para um inteiro
print("umFloat ao quadrado ", umFloat*umFloat)
