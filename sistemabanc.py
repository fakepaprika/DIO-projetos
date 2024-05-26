#quero guardar os valores 
import time
print('''        --- MENU---
        [d] - depósito
        [s] - saque
        [e] - extrato
        [q] - sair
        ''')
saldo=0
nsaques=0
extrato = ""
limite=500

LIMITE_SAQUES=3

while True:

    operação = input("Digite uma opção do menu:")
    


    if operação == "d":
        deposito = float(input("Qual valor desejar depositar em sua conta?"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito no valor de R$ {deposito:.2f}\n"
        print(f"O saldo atual é de R$ {saldo}.")
                
    elif operação == "s":
        if nsaques < LIMITE_SAQUES:

            saque = float(input("Digite o valaor que desejar extrair da conta:"))

            if saque <= limite:
                if saque <= saldo:
                    saldo-=saque
                    extrato+= f"Saque no valor de R$ {saque:.2f}\n"
                    nsaques+=1
                
                else:
                    print("Você não tem saldo suficiente para realizar o saque.")

            elif saque > limite:
                print("Limite de saque atingido.")

        else:
            print("Limite de saques diários atigindo.")
        
        print(f"O saldo atual é de R$ {saldo}.")

        
        
    elif operação == "e":
        if extrato == '':
            print("Não houve movimentação na conta.")
        else:
            print(extrato)
        print(f"O saldo atual é de R$ {saldo}.\n")   

    elif operação == "q":
        print("Finalizando operação...")
        time.sleep(2)
        print("Agradeçemos a confiança. Volte sempre!")
        break 