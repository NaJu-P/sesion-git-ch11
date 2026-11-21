def is_fibonacci(n: int) -> bool:
    contador = 1
    comprobacion = False
    calculo_1 = 5*(n*n)+4
    calculo_2 = 5*(n*n)-4
    resultado = contador**2

    while contador <= 89:
        print(resultado)

        if calculo_1 == resultado:
            print("si")
            comprobacion =  True
        
        elif calculo_2 == resultado:
            print("double si")
            comprobacion = True

        contador += 1

    return comprobacion

print(is_fibonacci(21))
