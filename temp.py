"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

"ALERTA!!! 🥵♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."
"""
#!/usr/bin/env python3

temp = float(input("Qual é a temperatura?"))
umidade = float(input("Qual a umidade do ar?"))
if temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 10:
    print("Frio")
elif temp < 0:
    print("ALERTA!!! Frio Extremo.")
