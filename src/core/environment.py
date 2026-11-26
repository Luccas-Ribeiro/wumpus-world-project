"""Contrato do ambiente"""

from abc import ABC, abstractmethod

from src.core.models import Action, Percept, Position


class Environment(ABC):
    """Mundo de Wumpus parcialmente observável"""

    @abstractmethod
    def reset(self, size: int, seed: int) -> None:
       """Gera um novo mundo de tamanho `size` x `size` a partir da seed."""


    @abstractmethod
    def step(self, action: Action) -> list[Percept]:
        """Aplica uma ação e devolve as percepções do novo estado.

        Também é o ponto em que o Wumpus pode se mover.
        """


    @abstractmethod
    def agent_position(self) -> Position:
        """Posição atual do agente."""


    @abstractmethod
    def is_over(self) -> bool:
        """True quando o epsódio terminou (com vitória, morte ou saída)."""


    @abstractmethod
    def score(self) -> int:
        """Pontuação acumulada até o momento."""


    @abstractmethod
    def arrows_left(self) -> int:
        """Flechas restantes (máximo 1)."""
