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

    return n in resultados

    

print(is_power_of_two(1))
print(is_power_of_two(16))
print(is_power_of_two(0))
print(is_power_of_two(6))
print(is_power_of_two(1024))