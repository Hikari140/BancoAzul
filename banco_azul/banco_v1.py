# Realizar a operação DEPÓSITO
# 1. depositar valores positivos
# 2. depósitos devem ser armazenados em uma variável extrato

# Realizar a operação SAQUE
# 3 saques diários com limite máximo de R$500,00 por saque.
# quantidade de saque diário
# limite máximo por saque
# Se não tiver saldo, não será possível sacar o dinheiro por
# falta de saldo.
# saques devem ser armazenados em uma variável extrato

# Realizar a operação EXTRATO
# listar todos os depósitos e saques realizados
# deve ser exibido o saldo atual da conta ao final
# em branco, exibir a mensagem: Não foram realizadas movimentações.
# R$ xxx.xx, exemplo:R$ 1500.45



#Escopo global
saldo = 1000
extrato = ""
numero_saques = 0


#Constantes
LIMITE_SAQUE = 500
LIMITE_DIARIO = 3

menu = """
        INFORME UMA OPÇÃO ABAIXO:
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
 
=>: """

while True:
    opcao = input(menu) # Escopo local

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))
        if valor > 0:
            # saldo = saldo + valor
            saldo += valor # Incremento
            extrato = extrato + f'Depósito: R${valor:.2f}\n'
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print("Operação Falhou. O valor informado é inválido!")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: R$"))
        
        excedeu_saldo = valor > saldo #Excedeu o valor do saldo
        excedeu_limite = valor > LIMITE_SAQUE #Excedeu o limite por saque (R$500)
        excedeu_saques = numero_saques >= LIMITE_DIARIO #Excedeu quantidade de saque (3)

        if excedeu_saldo:
            print("Operação Falhou. Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Operação Falhou. Você não tem saldo suficiente!")  
        elif excedeu_saques:
            print("Operação Falhou. Número de saques suficiente!")
        elif valor > 0:
            saldo -= valor #saldo = saldo - valor
            extrato = extrato + f'Saque: R${valor:.2f}\n'
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
            numero_saques += 1 # numero_saques = numero_saques + 1
        else:
            print("Operação Falhou. O valor informado é inválido!")
    
    elif opcao == "e":
        print("\n============ E X T R A T O ============")
        print("Não foram realizadas movimentações" if extrato == "" else extrato)
        print(f"\n Saldo Atual: R$ {saldo:.2f}")
        print("\n=======================================")
    
    elif opcao == "q":
        print ("Obrigado, volte sempre!")
        break # Utilizado para "quebrar" o loop
    else:
        print("Opção inválida. Por favor, selecione novamente a operação desejada.")