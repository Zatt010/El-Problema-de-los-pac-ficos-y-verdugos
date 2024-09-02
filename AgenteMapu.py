from AgenteIA.AgenteBuscadorConEstadisticas import AgenteBuscadorConEstadisticas
import time
class AgenteMapu(AgenteBuscadorConEstadisticas):
    def __init__(self):
        super().__init__()
        self.estado_inicial = (3, 3, 1)
        self.estado_meta = (0, 0, 0)
        self.acciones = []
        self.profundidad_maxima = 10
    
    def sucesores(self, estado):
        pafi_izq, verdug_izq, bt = estado
        pafi_der = 3 - pafi_izq
        verdug_der = 3 - verdug_izq
        sucesores = []

        def es_estado_valido(p_izq, v_izq, p_der, v_der):
            return (p_izq == 0 or p_izq >= v_izq) and (p_der == 0 or p_der >= v_der)

        if bt == 1:
            if pafi_izq > 0 and es_estado_valido(pafi_izq - 1, verdug_izq, pafi_der + 1, verdug_der):
                sucesores.append(((pafi_izq - 1, verdug_izq, 0), "Llevar 1 pacífico al lado derecho"))
            if verdug_izq > 0 and es_estado_valido(pafi_izq, verdug_izq - 1, pafi_der, verdug_der + 1):
                sucesores.append(((pafi_izq, verdug_izq - 1, 0), "Llevar 1 verdugo al lado derecho"))
            if pafi_izq > 0 and verdug_izq > 0 and es_estado_valido(pafi_izq - 1, verdug_izq - 1, pafi_der + 1, verdug_der + 1):
                sucesores.append(((pafi_izq - 1, verdug_izq - 1, 0), "Llevar 1 pacífico y 1 verdugo al lado derecho"))
            if pafi_izq > 1 and es_estado_valido(pafi_izq - 2, verdug_izq, pafi_der + 2, verdug_der):
                sucesores.append(((pafi_izq - 2, verdug_izq, 0), "Llevar 2 pacíficos al lado derecho"))
            if verdug_izq > 1 and es_estado_valido(pafi_izq, verdug_izq - 2, pafi_der, verdug_der + 2):
                sucesores.append(((pafi_izq, verdug_izq - 2, 0), "Llevar 2 verdugos al lado derecho"))
        else:
            if pafi_der > 0 and es_estado_valido(pafi_izq + 1, verdug_izq, pafi_der - 1, verdug_der):
                sucesores.append(((pafi_izq + 1, verdug_izq, 1), "Llevar 1 pacífico de vuelta al lado izquierdo"))
            if verdug_der > 0 and es_estado_valido(pafi_izq, verdug_izq + 1, pafi_der, verdug_der - 1):
                sucesores.append(((pafi_izq, verdug_izq + 1, 1), "Llevar 1 verdugo de vuelta al lado izquierdo"))
            if pafi_der > 0 and verdug_der > 0 and es_estado_valido(pafi_izq + 1, verdug_izq + 1, pafi_der - 1, verdug_der - 1):
                sucesores.append(((pafi_izq + 1, verdug_izq + 1, 1), "Llevar 1 pacífico y 1 verdugo de vuelta al lado izquierdo"))
            if pafi_der > 1 and es_estado_valido(pafi_izq + 2, verdug_izq, pafi_der - 2, verdug_der):
                sucesores.append(((pafi_izq + 2, verdug_izq, 1), "Llevar 2 pacíficos de vuelta al lado izquierdo"))
            if verdug_der > 1 and es_estado_valido(pafi_izq, verdug_izq + 2, pafi_der, verdug_der - 2):
                sucesores.append(((pafi_izq, verdug_izq + 2, 1), "Llevar 2 verdugos de vuelta al lado izquierdo"))

        return sucesores

    def es_meta(self, estado):
        return estado == self.estado_meta

    def programa(self, tecnica=None):
        if tecnica is not None:
            self.tecnica = tecnica
        
        frontera = [(self.estado_inicial, [])]
        visitado = set()
        start_time = time.time()

        while frontera:
            self.max_frontera_size = max(self.max_frontera_size, len(frontera))
            
            if self.tecnica == "amplitud":
                estado, acciones = frontera.pop(0)  # Búsqueda en amplitud (FIFO)
            else:
                estado, acciones = frontera.pop()  # Búsqueda en profundidad (LIFO)

            if self.es_meta(estado):
                self.acciones = acciones
                end_time = time.time()
                self.ejecucion_tiempo = end_time - start_time
                return
            
            if estado in visitado:
                continue
            
            visitado.add(estado)

            for sucesor, accion in self.sucesores(estado):
                if sucesor not in visitado:
                    frontera.append((sucesor, acciones + [accion]))

        self.acciones = ["No se encontró solución"]
        end_time = time.time()
        self.ejecucion_tiempo = end_time - start_time
