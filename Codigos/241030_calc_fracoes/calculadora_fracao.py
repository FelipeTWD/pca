from math import gcd
from fracao import Fracao

class Calculadora_Fracao:
    
    # método construtor.
    def __init__(self, fracao1: Fracao, fracao2: Fracao) -> None:

        self.fracao1: Fracao = fracao1
        self.fracao2: Fracao = fracao2
        
    def multiplicar(self) -> Fracao:
        resultado: Fracao
        resultado = Fracao(self.fracao1.numerador * self.fracao2.numerador,
                        self.fracao1.denominador * self.fracao2.denominador)
        
        return self._simplificar(resultado)
    
    def dividir(self) -> Fracao:
        resultado: Fracao
        resultado = Fracao(self.fracao1.numerador * self.fracao2.denominador,
                        self.fracao1.denominador * self.fracao2.numerador)
        
        return self._simplificar(resultado)
    
    def somar(self) -> Fracao:
        resultado: Fracao
        
        resultado = Fracao(self.fracao1.numerador * self.fracao2.denominador + self.fracao2.numerador * self.fracao1.denominador, self.fracao1.denominador * self.fracao2.denominador)
        
        return self._simplificar(resultado)
    
    def subtrair(self) -> Fracao:
        resultado: Fracao
        resultado = Fracao(self.fracao1.numerador * self.fracao2.denominador - self.fracao2.numerador * self.fracao1.denominador, self.fracao1.denominador * self.fracao2.denominador)
        
        return self._simplificar(resultado)
    
    def _simplificar(self, fracao: Fracao) -> Fracao:
        # calculo o MDC (Máximo Divisor Comum) entre o numerador e o denominador.
        mdc: int = gcd(fracao.numerador, fracao.denominador)
        
        # crio uma nova fração simplificada.
        frac_simplificada: Fracao = \
            Fracao(fracao.numerador // mdc, fracao.denominador // mdc)
            
        return frac_simplificada