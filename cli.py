from controllers.transaction_controller import TransactionController
from dtos.transaction_dto import TransactionDto
from enums.transaction_enum import TransactionType


def main():
    controller = TransactionController()
    while True:
        print("=" * 30)
        print("            Menu")
        print("-" * 30)
        print("1. Adicionar Entrada")
        print("2. Listar Entradas")

        print("3. Adicionar Despesa")
        print("4. Listar despesas")
        print("5. Adicionar Categoria")
        print("6. Listar categorias")
        print("=" * 30)

        print("Q. Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                descricao = input("Descrição da Entrada: ")
                valor = float(input("Valor: "))
                categoria_id = input("Agora escolha o id da categoria: ")

                controller.create_transaction(
                    TransactionDto(
                        description=descricao,
                        value=valor,
                        category_id=categoria_id,
                        type=TransactionType.INCOME
                    )
                )

            case "2":
                ...
            case "Q":
                break


if __name__ == "__main__":
    main()
