# gastos.py
# Lee un archivo .txt con montos de gastos y calcula el total y promedio

with open("gastos.txt", "r") as archivo:
    valores = [float(linea.strip()) for linea in archivo if linea.strip()]

total = sum(valores)
promedio = total / len(valores)

print(f"Total de gastos: ${total:.2f}")
print(f"Promedio de gastos: ${promedio:.2f}")

