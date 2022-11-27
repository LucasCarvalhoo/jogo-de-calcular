from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade desejado[1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print(f'Informe o resultado da seguinte operação:')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar? [1 - sim ou 0 - não] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print('Até a próxima!')


if __name__ == '__main__':
    main()