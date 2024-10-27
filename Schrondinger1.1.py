# Dicionário que armazena os usuários cadastrados e suas senhas
usuarios_cadastrados = {'usuario1': 'senha1', 'usuario2': 'senha2', 'medico1': 'senha3'}

# Lista de postagens aleatórias sobre saúde
postagens_saude = [
    {"titulo": "Dicas para uma vida saudável", "conteudo": "Mantenha uma dieta equilibrada e pratique exercícios regularmente."},
    {"titulo": "Importância do sono", "conteudo": "Dormir bem é crucial para a saúde mental e física."},
    {"titulo": "Benefícios da hidratação", "conteudo": "Beber água suficiente ajuda no funcionamento adequado do corpo."},
]

# Localizações de farmácias pré-definidas
farmacias_proximas = [
    {"nome": "Santa Catarina", "latitude": -27.5969, "longitude": -48.5495},
    {"nome": "Drogaria Sao Paulo", "latitude": -27.5970, "longitude": -48.5485},
    {"nome": "Drogaria Santa Cruz", "latitude": -27.5980, "longitude": -48.5475},
    {"nome": "Drogaria Farmed", "latitude": -27.5990, "longitude": -48.5465},
]

def fazer_cadastro():
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    while True:
        try:
            perfil = input("Escolha o perfil (Paciente/Médico): ").capitalize()

            if perfil == "Médico":
                crm = input("Digite o CRM: ")
                usuarios_cadastrados[nome.lower()] = {'senha': senha, 'perfil': perfil, 'crm': crm}
                print("Cadastro realizado com sucesso!")
                break
            elif perfil == "Paciente":
                usuarios_cadastrados[nome.lower()] = {'senha': senha, 'perfil': perfil}
                print("Cadastro realizado com sucesso!")
                break
            else:
                print("Digite uma opção válida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def fazerLogin(usuarios_cadastrados):
    nome = input("\nDigite seu nome: ")

    while nome.lower() not in usuarios_cadastrados:
        print("Usuário não cadastrado")
        nome = input("Digite seu nome novamente: ")

    senha = input("\nDigite sua senha: ")
    senha_armazenada = usuarios_cadastrados[nome.lower()]['senha']

    while senha != senha_armazenada:
        print("Senha incorreta")
        senha = input("Digite sua senha novamente: ")

    print("\nSeja bem-vindo ao Dr.Avisa!")

def exibir_postagens():
    print("\n** Postagens sobre Saúde **")
    for postagem in postagens_saude:
        print(f"\nTitulo: {postagem['titulo']}\nConteúdo: {postagem['conteudo']}\n")

def criar_postagem():
    titulo = input("Digite o título da postagem: ")
    conteudo = input("Digite o conteúdo da postagem: ")
    anexo_imagem = input("Digite o caminho do anexo de imagem (ou deixe em branco se não houver): ")

    nova_postagem = {"titulo": titulo, "conteudo": conteudo}
    postagens_saude.append(nova_postagem)
    print("\nPostagem criada com sucesso!")

def localizar_farmacia():
    print("\nFarmácias próximas:")
    for i, farmacia in enumerate(farmacias_proximas, start=1):
        print(f"{i}. {farmacia['nome']}")

    escolha_farmacia = int(input("\nEscolha o número da farmácia desejada: "))
    farmacia_escolhida = farmacias_proximas[escolha_farmacia - 1]

    print(f"\nVocê escolheu a farmácia {farmacia_escolhida['nome']}.")
    print(f"A localização é aproximadamente em ({farmacia_escolhida['latitude']}, {farmacia_escolhida['longitude']}).")
    print("Tempo estimado de chegada: 10 minutos (simulação)")

def agendar_consulta():
    print("\nAgendamento Confirmado:")
    especialidades = ["Cardiologia", "Dermatologia", "Ortopedia", "Pediatria"]
    doutores = ["Dr. Silva", "Dra. Santos", "Dr. Oliveira", "Dra. Lima"]
    horarios = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
    formas_pagamento = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito"]

    especialidade = escolher_opcao("Especialidade", especialidades)
    data = input("Data da Consulta: ")
    doutor = escolher_opcao("Doutor", doutores)
    horario = escolher_opcao("Horário", horarios)
    forma_pagamento = escolher_opcao("Forma de Pagamento", formas_pagamento)

    print(f"Especialidade: {especialidade}")
    print(f"Data: {data}")
    print(f"Doutor: {doutor}")
    print(f"Horário: {horario}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print(f"Consulta Marcada!")

def escolher_opcao(pergunta, opcoes):
    print(f"\nEscolha {pergunta}:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    while True:
        try:
            escolha = int(input(f"Digite o número da {pergunta} desejada: "))
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    fazer_cadastro()
    print("\nBem-vindo ao DR.Avisa")
    fazerLogin(usuarios_cadastrados)
    exibir_postagens()

    while True:
        print("\n** Menu Principal **")
        print("1. Criar Postagem")
        print("2. Localizar Farmácia")
        print("3. Agendar Consulta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_postagem()
            exibir_postagens()
        elif opcao == "2":
            localizar_farmacia()
        elif opcao == "3":
            agendar_consulta()
        elif opcao == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()