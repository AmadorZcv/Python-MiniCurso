# Exercicio 1
# Trocar as variaveis numericas abaixo
A = 20
B = 7
# Solução 1 - Simples
print("Solução 1 - Simples")
C = A
A = B
B = C
print("A variavel A é igual a : ", A, " E a variavel B é igual a: ", B)
# Solução 2 - Solução Matematica(Só funciona com numeros)
print("Solução 2 - Poder da Matematica")
A = 20
B = 7
# A agora é 27
A = A + B
# B agora é 20
B = A - B
# A agora é 7
A = A - B
print("A variavel A é igual a : ", A, " E a variavel B é igual a: ", B)
# Solução 3 - Conceitos mais avançados de programação
print("Solução 3 - Conceitos mais avançados de programação")
A = 20
B = 7
B, A = A, B
print("A variavel A é igual a : ", A, " E a variavel B é igual a: ", B)
# Resultado esperado
# A variavel A é igual a :  7  E a variavel B é igual a:  20

# Exercicio 2
# Receba o valor da base e da altura de um triangulo Isósceles e retorne a sua area
# Solução
# O exercicio tem varias maneiras de ser resolvido, ele está correto desde que:
# O dado seja pego do usuario de forma correta,pegando com input e convertendo depois
# E a formula seja empregada corretamente
base, altura = float(input("Digite a base e a altura do triangulo")), float(
    input("Digite a altura do triangulo"))
area = base*altura/2
print("A area do triangulo é ", area)

# Existe uma maneira que economiza mais codigo ainda
# Porém quando escrevemos codigo não devemos pensar somente na resolução do problema
# Mas tambem na manutenção do codigo e na sua habilidade de ler ele depois
# Esta solução abaixo acaba sendo dificil de compreender,mesmo resolvendo o problema
# Devemos sempre tentar ser o mais claros possiveis no codigo e utilizar soluções simples quando possivel
print("A area do triangulo com codigo super compacto é ",
      (float(input("Digite a base e a altura do triangulo")) * float(input("Digite a altura do triangulo")))/2)
