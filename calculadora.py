primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operacao = str(input("Digite a operação(+ ou - ou * ou /): "))

if operacao == "+":
  soma = primeiro_numero + segundo_numero
  print(soma)

elif operacao == "-":
  diminuicao = primeiro_numero - segundo_numero
  print(diminuicao)

elif operacao == "*":
  multiplicacao = primeiro_numero * segundo_numero
  print(multiplicacao)

elif operacao == "/":
  divisao = primeiro_numero / segundo_numero
  print(divisao)