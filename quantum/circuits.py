from discopy import Dim

from lambeq.tensor import SpiderAnsatz
from lambeq.core.types import AtomicType


class Circuit:

    ansatz = SpiderAnsatz({AtomicType.NOUN: Dim(2),
                           AtomicType.SENTENCE: Dim(2)})

    def create_circuit(self, diagram):
        print('Creating circuits...')
        circuits = [self.ansatz(d) for d in diagram]

        return circuits

    def draw_circuits(self, circuits):
        for i in enumerate(circuits):
            self.draw_circuit(circuits, i)

    def draw_circuit(self, circuits, i):
        circuits[i].draw()
