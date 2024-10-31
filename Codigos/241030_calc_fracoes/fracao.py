class Fracao:
    
    # método construtor.
    def __init__(self, numerador: int, denominador: int) -> None:
        
        if denominador == 0:
            raise ValueError('Denominador não pode ser zero.')
        
        self.numerador: int = numerador
        self.denominador: int = denominador
        
    def transformar_decimal(self) -> float:
        return self.numerador / self.denominador
    
    def __str__(self) -> str:
        return f'{self.numerador}/{self.denominador}'