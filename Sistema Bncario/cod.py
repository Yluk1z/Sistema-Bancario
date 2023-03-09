menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 600
numeros_saque = 0
LIMITE_DE_SAQUE = 3
extrato = 0

while True:

  opcao_menu =  input (f"{menu} Digite uma opção:")

  if opcao_menu == "1":
    valor_deposito = int(input("Valor do deposito: R$"))

    if valor_deposito > 0:
      saldo += valor_deposito
      extrato += valor_deposito
      print(f"deposito realizado com suesso no valor R$ {valor_deposito}!")
  
    else:
     print("Operação falhou, Numero digitado invalido!")

  elif opcao_menu == "2":
    valor_de_saque = int(input("Qual valor desejado do saque:"))
    
    validação_saldo = valor_de_saque > saldo

    validação_limite = valor_de_saque > limite

    validação_limite_de_saque = numeros_saque >= LIMITE_DE_SAQUE

    if validação_saldo:
      print("Operação falhou, saldo insuficiente!")

    elif validação_limite:
      print ("Operação falhou, limite de saque de 600 reais atingido!")
    
    elif validação_limite_de_saque:
      print("Operação falhou, limite de 3 saques diarios atingido!")

    elif valor_de_saque > 0:
      saldo -= valor_de_saque
      extrato -= valor_de_saque
      print(f"Operação realizada com sucesso, seu saque foi de R$ {valor_de_saque}")
      numeros_saque += 1 
      
    else:
      print("O valor digitado é invalido!")
  
  if opcao_menu == "3":
      print(f"Seu saldo é R${extrato}")

  elif opcao_menu == "4":
    break

else:
    print("operação invalida, por favor selecionar novamente a operação desejada!")
  
