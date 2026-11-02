def is_power_of_two(n: int) -> bool:
    
    resultados = [
        2**0,
        2**1,
        2**2,
        2**3,
        2**4,
        2**5,
        2**6,
        2**7,
        2**8,
        2**9,
        2**10
    ]

    for resultados_1 in resultados:
        print(resultados_1)
        
        if resultados_1 == n:
            return True

        else:
            return False

print(is_power_of_two(6))