def is_fibonacci(n: int) -> bool:
    
    calculo = pow(5*(n*n)+4, 0.5)
    
    if calculo.is_integer():
        calculo = int(calculo)
        
    if isinstance(calculo, int):
        return True
    
    else:
        return False
