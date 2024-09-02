# **********************************************************
# * Clase: Agente buscador                                 *
# * Autor: Victor Estevez                                  *
# * Version: v2023.03.29                                   *
# * Descripcion: Implementacion de algoritmos de busqueda  *
# *              sin informacion y con informacion         *
# **********************************************************

from AgenteIA.Agente import Agente
from copy import deepcopy

class AgenteBuscador(Agente):
    def __init__(self):
        super().__init__()
        self.estado_inicial = None
        self.estado_meta = None
        self.funcion_sucesor = []
        self.tecnica = None

    def add_funcion(self, f):
        self.funcion_sucesor.append(f)

    def test_objetivo(self, e):
        return e == self.estado_meta

    def generar_hijos(self, e):
        hijos = []
        for fun in self.funcion_sucesor:
            h = fun(e)
            if h:
                hijos.append(h)
        return hijos

    def get_costo(self, camino):
        return len(camino) - 1

    def get_heuristica(self, camino):
        pac, ver, _ = camino[-1]
        return pac + ver

    def get_funcion_a(self, camino):
        return self.get_costo(camino) + self.get_heuristica(camino)

    def programa(self):
        frontera = [[self.estado_inicial]]
        visitados = set()

        while frontera:
            if self.tecnica == "profundidad":
                camino = frontera.pop()
            else:
                camino = frontera.pop(0)  # Asumiendo amplitud aquí

            nodo = camino[-1]

            if self.test_objetivo(nodo):
                self.acciones = camino
                break

            if nodo not in visitados:
                visitados.add(nodo)
                for hijo in self.generar_hijos(nodo):
                    aux = deepcopy(camino)
                    aux.append(hijo)
                    frontera.append(aux)

                if self.tecnica == "costouniforme":
                    frontera.sort(key=lambda tup: self.get_costo(tup))
                elif self.tecnica == "codicioso":
                    frontera.sort(key=lambda tup: self.get_heuristica(tup))
                elif self.tecnica == "a_estrella":
                    frontera.sort(key=lambda tup: self.get_funcion_a(tup))
