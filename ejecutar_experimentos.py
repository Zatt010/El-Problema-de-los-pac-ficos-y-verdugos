from AgenteMapu import AgenteMapu
import random

def ejecutar_experimentos(num_experimentos):
    resultados = {
        "profundidad": {
            "soluciones_encontradas": 0,
            "tiempo_total": 0,
            "max_frontera_size": 0
        },
        "amplitud": {
            "soluciones_encontradas": 0,
            "tiempo_total": 0,
            "max_frontera_size": 0
        }
    }

    for _ in range(num_experimentos):
        estado_inicial = generar_estado_inicial()
        
        # Búsqueda en amplitud
        agente_amplitud = AgenteMapu()
        agente_amplitud.tecnica = "amplitud"
        agente_amplitud.estado_inicial = estado_inicial
        agente_amplitud.programa(tecnica="amplitud")
        
        if agente_amplitud.acciones and agente_amplitud.acciones[0] != "No se encontró solución":
            resultados["amplitud"]["soluciones_encontradas"] += 1
        resultados["amplitud"]["tiempo_total"] += agente_amplitud.ejecucion_tiempo
        resultados["amplitud"]["max_frontera_size"] = max(resultados["amplitud"]["max_frontera_size"], agente_amplitud.max_frontera_size)

        # Búsqueda en profundidad
        agente_profundidad = AgenteMapu()
        agente_profundidad.tecnica = "profundidad"
        agente_profundidad.estado_inicial = estado_inicial
        agente_profundidad.programa(tecnica="profundidad")
        
        if agente_profundidad.acciones and agente_profundidad.acciones[0] != "No se encontró solución":
            resultados["profundidad"]["soluciones_encontradas"] += 1
        resultados["profundidad"]["tiempo_total"] += agente_profundidad.ejecucion_tiempo
        resultados["profundidad"]["max_frontera_size"] = max(resultados["profundidad"]["max_frontera_size"], agente_profundidad.max_frontera_size)

    resultados["profundidad"]["probabilidad_solucion"] = resultados["profundidad"]["soluciones_encontradas"] / num_experimentos
    resultados["amplitud"]["probabilidad_solucion"] = resultados["amplitud"]["soluciones_encontradas"] / num_experimentos
    
    resultados["profundidad"]["tiempo_promedio"] = resultados["profundidad"]["tiempo_total"] / num_experimentos
    resultados["amplitud"]["tiempo_promedio"] = resultados["amplitud"]["tiempo_total"] / num_experimentos
    
    return resultados

def generar_estado_inicial():
    while True:
        pafi_izq = random.randint(0, 3)
        verdug_izq = random.randint(0, 3)
        bt = random.choice([0, 1])
        pafi_der = 3 - pafi_izq
        verdug_der = 3 - verdug_izq

        if (pafi_izq == 0 or pafi_izq >= verdug_izq) and (pafi_der == 0 or pafi_der >= verdug_der):
            return (pafi_izq, verdug_izq, bt)

if __name__ == "__main__":
    num_experimentos = 1000
    resultados = ejecutar_experimentos(num_experimentos)

    print("Resultados de búsqueda en profundidad:")
    print(f"Probabilidad de encontrar solución: {resultados['profundidad']['probabilidad_solucion']:.2f}")
    print(f"Tiempo promedio: {resultados['profundidad']['tiempo_promedio']:.2f} segundos")
    print(f"Tamaño máximo promedio de la frontera: {resultados['profundidad']['max_frontera_size']:.2f}")

    print("\nResultados de búsqueda en amplitud:")
    print(f"Probabilidad de encontrar solución: {resultados['amplitud']['probabilidad_solucion']:.2f}")
    print(f"Tiempo promedio: {resultados['amplitud']['tiempo_promedio']:.2f} segundos")
    print(f"Tamaño máximo promedio de la frontera: {resultados['amplitud']['max_frontera_size']:.2f}")
