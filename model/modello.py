from functools import lru_cache
from time import time
import copy

class Model:
    def __init__(self):
        self.lista_soluzioni = []
        self.set_soluzioni = None

    def calcola_anagrammi(self, parola: str):
        self.lista_soluzioni = []
        self.set_soluzioni = set()
        self._ricorsione("", parola)
        # controllo parole corrette
        return self.set_soluzioni

    def calcola_anagrammi_list(self, parola: str):
        self.lista_soluzioni = []
        self._ricorsione_list([], parola)
        return self.lista_soluzioni

    def _ricorsione(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            self.set_soluzioni.add(parziale)
        else:
            for i in range(len(rimanenti)):
                parziale += rimanenti[i]
                # chiamare la ricorsione con parziale e tutte le lettere rimanenti meno lettera
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione(parziale, nuove_rimanenti)
                parziale = parziale[:-1] # ----> BACKTRACKING
        return self.set_soluzioni

    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            self.lista_soluzioni.append(copy.deepcopy(parziale))
        else:
            for i in range(len(rimanenti)):
                parziale.append(rimanenti[i])
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione_list(parziale, nuove_rimanenti)
                parziale.pop() # ----> BACKTRACKING
        return self.lista_soluzioni


if __name__ == '__main__':
    model = Model()
    start = time()
    print("Anagrammi di dog:", model.calcola_anagrammi("dog"))
    end = time()
    print(f"Elapsed time: {end - start} seconds")
    print("Anagrammi di casa:", model.calcola_anagrammi("casa"))
    print(model.calcola_anagrammi_list("casa"))