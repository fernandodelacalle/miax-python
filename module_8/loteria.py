
import random
import time

start_time = time.time()

combinaciones = 50000
n_bolas = 5

def sacar_bola_slow(combi, n_bola):
    "Esta forma produce bolas repetidas y hay que buscarlas"
    bola = random.randint(0, 50)
    for bola_comp in range(n_bola):
        if bola == combi[bola_comp]:
            bola = random.randint(0, 50)
    return bola

combi_ganadora = []
for i in range(n_bolas):
    combi_ganadora.append(sacar_bola_slow(combi_ganadora, i))

apuestas = []
aciertos = []

for combinancion in range(combinaciones):
    combi_apostada = []
    for n_bola in range(n_bolas):
        combi_apostada.append(sacar_bola_slow(combi_apostada, n_bola))
    apuestas.append(combi_apostada)
    
    aciertos_combinacion = 0
    for bola_ganadora in combi_ganadora:
        for bola_apostada in combi_apostada:
            if bola_ganadora == bola_apostada:
                aciertos_combinacion += 1
    aciertos.append(aciertos_combinacion)

for num_aciertos in range(n_bolas):
    print(f"{num_aciertos} : {aciertos.count(num_aciertos)}")

print("--- %s seconds ---" % (time.time() - start_time))
