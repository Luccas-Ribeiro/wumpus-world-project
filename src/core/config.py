"""Configuração de um mundo de Wumpus."""

import random
from dataclasses import dataclass

MIN_SIZE = 4
DEFAULT_PIT_RATIO = 0.2


def random_seed() -> int:
    """Sorteia uma seed. Deve ser chamada antes de criar a config, e a seed
    sorteada precisa ser exibida e guardada para permitir refazer o mundo."""
    return random.randrange(2**31)


@dataclass(frozen=True)
class WorldConfig:
    """Parâmetros de um mundo.

    A quantidade de poços é opcional. Se `pit_count` não for informado, o
    mundo recebe uma quantidade proporcional ao tamanho da grade, calculada
    com DEFAULT_PIT_RATIO.
    """

    size: int                          # tamanho da grade, size x size
    seed: int                          # seed usada para gerar o mundo
    pit_count: int | None = None       # quantidade fixa de poços
    wumpus_move_every: int = 1         # k: o wumpus se move a cada k turnos (k >= 1)

    def __post_init__(self) -> None:
        if self.size < MIN_SIZE:
            raise ValueError(f"size deve ser pelo menos {MIN_SIZE}, recebido {self.size}")

        if self.pit_count is not None and not 0 <= self.pit_count < self.free_cells():
            raise ValueError(
                f"pit_count deve estar entre 0 e {self.free_cells() - 1}, recebido {self.pit_count}")

        if self.wumpus_move_every < 1:
            raise ValueError("wumpus_move_every deve ser pelo menos 1")

    def free_cells(self) -> int:
        """Células que podem receber poço: todas, menos a do início."""
        return self.size * self.size - 1

    def resolved_pit_count(self) -> int:
        """Quantidade efetiva de poços."""
        if self.pit_count is not None:
            return self.pit_count

        return max(1, round(DEFAULT_PIT_RATIO * self.free_cells()))
