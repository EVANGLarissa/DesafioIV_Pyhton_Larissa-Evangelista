from datetime import date


class Funcionario:

    def __init__(self, name, dt_contratacao, salario):
        self.name = name
        self.dt_contratacao = dt_contratacao
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def exibir_dados(self):
        print(
            f"Nome: {self.name} | Salário: R$ {self.salario:.2f} | Data de Contratação: {self.dt_contratacao}"
        )


class Gerente(Funcionario):

    def aumentar_salario(self, percentual):
        hoje = date.today()
        anos_servico = hoje.year - self.dt_contratacao.year
        if (hoje.month, hoje.day) < (self.dt_contratacao.month,
                                     self.dt_contratacao.day):
            anos_servico -= 1

        percentual_total = percentual + anos_servico
        aumento = self.salario * (percentual_total / 100)
        self.salario += aumento


def main():
    tipo = input("Cadastrar Funcionário(F) ou Gerente?(G): ").strip().upper()
    name = input("Nome: ")

    ano = int(input("Ano em que foi contratado: "))
    mes = int(input("Mês em que foi contratado (1 a 12): "))
    dia = int(input("Dia em que foi contratado: "))

    salario = float(input("Salário: R$ "))
    percentual = float(input("Percentual do aumento: "))

    dt_contratacao = date(ano, mes, dia)

    if tipo.lower() in ['g', 'gerente']:
        funcionario = Gerente(name, dt_contratacao, salario)
    else:
        funcionario = Funcionario(name, dt_contratacao, salario)

    print("\nAntes do aumento:")
    funcionario.exibir_dados()

    funcionario.aumentar_salario(percentual)

    print("\nDepois do aumento:")
    funcionario.exibir_dados()


if __name__ == "__main__":
    main()
