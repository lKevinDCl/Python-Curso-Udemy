capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

conjunto = zip(capitales,paises)

for capitales, paises in conjunto:
    print(f"La capital de {paises} es {capitales}")




espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espaniol, portugues, ingles))

print(numeros)
