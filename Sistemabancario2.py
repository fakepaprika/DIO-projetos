import time
contas = []
saldo=0
nsaques=0
extrato = ""
limite=500
LIMITE_SAQUES=3

def fazer_deposito():
    global saldo
    global extrato
    deposito = float(input("Qual valor desejar depositar em sua conta?"))
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito no valor de R$ {deposito:.2f}\n"
    print(f"O saldo atual é de R$ {saldo}.")

def fazer_saque():
    global saldo
    global LIMITE_SAQUES
    global extrato
    global nsaques

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

def ver_extrato():
    global extrato
    if extrato == '':
        print("Não houve movimentação na conta.")
    else:
        print(extrato)
    print(f"O saldo atual é de R$ {saldo}.\n")  

def sair():
    print("Finalizando operação...")
    time.sleep(2)
    print("Agradeçemos a confiança. Volte sempre!")

def criar_conta():
    global contas
    usuario = []
    print("Seja bem vindo! Vamos criar uma conta:")
    nome=input("Digite seu nome completo:")
    cpf = input("Digite seu CPF:")
    data= input("Digite sua data de nascimento:")
    endereço = input("Digite seu endereço (sigla estado - cidade - logradouro - bairro - numero):")
    usuario.extend([nome,cpf,data,endereço])
    contas.append(usuario)
    return usuario

def verificar_usuario(nome,lista):
    for usuario in lista:
        if usuario[0] == nome:
            print(f"Bem vindo {nome}")
            return True
        
    print("Você ainda não possui uma conta.")
    return False

while True:
    print('''=========BANCO===========
        [1] Já tenho uma conta
        [2] Criar conta''')

    inicio = input("Digite uma opação:")
    if inicio == "1":
        iniciar_usuario = input("Digite seu nome:")
        if verificar_usuario(iniciar_usuario,contas):
       
            while True:
                print('''        --- MENU ---
            [d] - depósito
            [s] - saque
            [e] - extrato
            [q] - sair
            ''')

                operação = input("Digite a operação que deseja realizar:")

                if operação == "d":
                    fazer_deposito()
                elif operação == "s":
                    fazer_saque()
                elif operação == "e":
                    ver_extrato()
                elif operação =="q":
                    sair()
                    break

    elif inicio == "2":
        criar_conta()
        print("Conta criada com sucesso!")
