from AgenteIA.AgenteBuscador import AgenteBuscador
import time

class AgenteBuscadorConEstadisticas(AgenteBuscador):
    def __init__(self):
        super().__init__()
        self.max_frontera_size = 0
        self.ejecucion_tiempo = 0
        self.tecnica = "amplitud"  # Por defecto, se usa búsqueda en amplitud
    
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
            elif self.tecnica == "profundidad":
                estado, acciones = frontera.pop()  # Búsqueda en profundidad (LIFO)
            else:
                raise ValueError("Técnica de búsqueda desconocida: debe ser 'amplitud' o 'profundidad'")
            
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
