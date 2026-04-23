from dataclasses import dataclass

# Exceções Personalizadas

class PesoInvalidoException(Exception):
    pass

class CapacidadeExcedidaException(Exception):
    pass

class ClienteNaoEncontradoException(Exception):
    pass



# Herança (3 níveis)

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)


class ClientePremium(Cliente):
    def __init__(self, nome: str, cpf: str, desconto: float):
        super().__init__(nome, cpf)
        self.desconto = desconto



# Herança Múltipla

class Seguro:
    def validar_seguro(self):
        return "Seguro válido"



# Polimorfismo

class Transporte:
    def __init__(self, capacidade: float):
        self.capacidade = capacidade

    def calcular_custo(self):
        return 0

    def tipo_transporte(self):
        return "Transporte genérico"

    def emitir_relatorio(self):
        return "Relatório padrão"


class Van(Transporte, Seguro):
    def __init__(self, capacidade: float):
        super().__init__(capacidade)
        self.portas = 4
        self.consumo = 10

    def calcular_custo(self):
        return 50

    def tipo_transporte(self):
        return "Van (transporte leve)"

    def emitir_relatorio(self):
        return "Utilizada para pequenas cargas"


class Caminhao(Transporte, Seguro):
    def __init__(self, capacidade: float):
        super().__init__(capacidade)
        self.eixos = 6
        self.consumo = 5

    def calcular_custo(self):
        return 150

    def tipo_transporte(self):
        return "Caminhão (transporte pesado)"

    def emitir_relatorio(self):
        return "Utilizado para grandes cargas"


class Onibus(Transporte, Seguro):
    def __init__(self, capacidade: float):
        super().__init__(capacidade)
        self.assentos = 40
        self.ar_condicionado = True

    def calcular_custo(self):
        return 100

    def tipo_transporte(self):
        return "Ônibus (transporte coletivo)"

    def emitir_relatorio(self):
        return "Utilizado para transporte de passageiros"


# Armazenamento (Coleções)

clientes = {}
transportes = []


# Funções

def cadastrar_cliente():
    try:
        nome = input("Nome: ")
        cpf = input("CPF: ")

        # Validação de dados vazios
        if not nome or not cpf:
            raise ClienteNaoEncontradoException("Dados inválidos!")

        # Validação de CPF duplicado
        if cpf in clientes:
            print("Cliente já cadastrado!")
            return

        tipo = input("Cliente Premium? (s/n): ").lower()

        if tipo == "s":
            desconto = float(input("Desconto: "))
            cliente = ClientePremium(nome, cpf, desconto)
        else:
            cliente = Cliente(nome, cpf)

        clientes[cpf] = cliente

    except ValueError:
        print("Erro: valor inválido!")

    except ClienteNaoEncontradoException as e:
        print("Erro:", e)

    else:
        print("Cliente cadastrado com sucesso!")

    finally:
        print("Operação finalizada.\n")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for c in clientes.values():
        print(f"{c.nome} - {c.cpf}")



# Lista de Compreensão

def listar_clientes_premium():
    premium = [c for c in clientes.values() if isinstance(c, ClientePremium)]

    if not premium:
        print("Nenhum cliente premium.")
        return

    for c in premium:
        print(f"{c.nome} (Desconto: {c.desconto})")


def cadastrar_transporte():
    try:
        capacidade = float(input("Capacidade: "))

        # Validação de capacidade
        if capacidade <= 0:
            raise PesoInvalidoException("Capacidade inválida!")

        if capacidade > 10000:
            raise CapacidadeExcedidaException("Capacidade excedida!")

        print("1 - Van | 2 - Caminhão | 3 - Ônibus")
        tipo = input("Escolha o tipo: ")

        match tipo:
            case "1":
                t = Van(capacidade)
            case "2":
                t = Caminhao(capacidade)
            case "3":
                t = Onibus(capacidade)
            case _:
                print("Tipo inválido!")
                return

        transportes.append(t)

    except ValueError:
        print("Digite um número válido!")

    except (PesoInvalidoException, CapacidadeExcedidaException) as e:
        print("Erro:", e)

    else:
        print("Transporte cadastrado!")

    finally:
        print("Fim da operação.\n")


def listar_transportes():
    if not transportes:
        print("Nenhum transporte cadastrado.")
        return

    for t in transportes:
        print(f"{t.tipo_transporte()} | Custo: {t.calcular_custo()}")
        # Uso do polimorfismo no relatório
        print(f"Relatório: {t.emitir_relatorio()}")
        # Uso da herança múltipla (seguro)
        print(f"Seguro: {t.validar_seguro()}")



# Menu (Match/Case)

def menu():
    while True:
        print("\n--- GERENCIADOR DE TRANSPORTES ---")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Listar clientes premium")
        print("4 - Cadastrar transporte")
        print("5 - Listar transportes")
        print("0 - Sair")

        opcao = input("Escolha: ")

        match opcao:
            case "1":
                cadastrar_cliente()
            case "2":
                listar_clientes()
            case "3":
                listar_clientes_premium()
            case "4":
                cadastrar_transporte()
            case "5":
                listar_transportes()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")



# Execução
if __name__ == "__main__":
    menu()
