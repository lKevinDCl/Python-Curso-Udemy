valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [ i for i in valores if i % 2 == 0  ]

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [((i - 32) * (5/9)) for i in temperatura_fahrenheit ]