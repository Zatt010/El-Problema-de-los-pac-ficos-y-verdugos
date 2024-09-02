# ******************************************************************
# * Clase: Entorno                                                 *
# * Autor: Victor Estevez                                          *
# * Version: v2023.03.29                                           *
# * Descripcion: Implementacion del entorno, proporciona           *
# *              percepciones a los agentes y ejecuta las acciones *
# *              de cada agente  que se encuentra en el            *
# ******************************************************************


class Entorno:
    def __init__(self):
        self.agentes = []
        self.objetos = set()

    def get_percepciones(self, agente):
        percepciones = {
            'pos_x': agente.estado_inicial[0],  # Suponiendo que pos_x y pos_y se derivan del estado
            'pos_y': agente.estado_inicial[1],
            'objetos': list(self.objetos)
        }
        agente.percepciones = percepciones
        agente.programa()

    def ejecutar(self, agente):
        if not agente.acciones:
            return
        
        # Asumiendo que las acciones están en formato de texto en la lista agente.acciones
        accion = agente.acciones.pop(0)
        print(f"Ejecutando acción: {accion}")
        # Aquí puedes ejecutar la acción en el entorno si es necesario.

    def evolucionar(self):
        for agente in self.agentes:
            self.get_percepciones(agente)
            self.ejecutar(agente)

    def run(self):
        while not self.finalizar():
            self.evolucionar()

    def finalizar(self):
        return all(agente.es_meta(agente.estado_inicial) for agente in self.agentes)

    def insertar(self, agente):
        self.agentes.append(agente)
