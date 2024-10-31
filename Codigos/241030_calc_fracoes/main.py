from fracao import Fracao
from calculadora_fracao import Calculadora_Fracao

def main() -> None:
    
    # 'fracao1' e 'fracao2' são OBJETOS da CLASSE Fracao.
    fracao1: Fracao = Fracao(2, 3)
    fracao2: Fracao = Fracao(4, 7)
    
    # 'calculadora' é um OBJETO da CLASSE Calculadora_Fracao.
    calculadora: Calculadora_Fracao = Calculadora_Fracao(fracao1, fracao2)
    resultado: Fracao = calculadora.somar()
    
    print(f'O resultado da multiplicação de {fracao1} por {fracao2} é: {resultado} e em decimal é: {resultado.transformar_decimal():.5f}')

if __name__ == '__main__':
    main()