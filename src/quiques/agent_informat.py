""" Fitxer que conté l'agent informat.

S'ha d'implementar el mètode:
    actua()
"""

from quiques.agent import Barca
from quiques.estat import Estat


class BarcaGreedy(Barca):
    def __init__(self):
        super(BarcaGreedy, self).__init__()
        self.__frontera = None
        self.__tancats = None
        self.__cami_exit = None

    def heuristica(self, estat: Estat) -> int:
        """
        Com menys animals queden a l'esquerra,
        més a prop consideram que estam de l'objectiu.
        """
        return estat.quica_esq + estat.llops_esq

    def cerca(self, estat_inicial: Estat) -> bool:
        
        self.__frontera = PriorityQueue()
        self.__tancats = set()

        contador = count()
        
        while not self.__frontera.empty():
            _, _, estat_actual = self.__frontera.get()

            # Ignoram estats repetits o no segurs
            if estat_actual in self.__tancats or not estat_actual.es_segur():
                continue

            # Comprovam si hem arribat a la meta
            if estat_actual.es_meta():
                self.__cami_exit = estat_actual.cami
                return True

            # Marcam l'estat com visitat
            self.__tancats.add(estat_actual)

            # Generam els fills
            for fill in estat_actual.genera_fill():

                if fill.es_segur() and fill not in self.__tancats:

                    self.__frontera.put(
                        (
                            self.heuristica(fill),
                            next(contador),
                            fill
                        )
                    )

        return False

    def actua(self, percepcio: dict) -> str | tuple[str, (int, int)]:

        if self.__cami_exit is None:

            estat_inicial = Estat(
                local_barca=percepcio["Lloc"],
                llops_esq=percepcio["Llop Esq"],
                polls_esq=percepcio["Poll Esq"],
            )

            self.cerca(estat_inicial)

        if self.__cami_exit:

            quiques, llops = self.__cami_exit.pop(0)

            return "M", (quiques, llops)

        else:
            return "A", None