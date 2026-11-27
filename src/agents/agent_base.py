"""Contrato do agente.

Todo agente (aleatório, humano, lógico e probabilístico) implementa essa interface. A GUI e o benchmark tratam todos da mesma forma.
"""

from abc import ABC, abstractmethod

from src.core.models import Action, Percept


class Agent(ABC):

    name: str

    @abstractmethod
    def reset(self, size: int) -> None:
        """Prepara o agente para um novo episódio em uma grade `size` x `size`."""


    @abstractmethod
    def act(self, percepts: list[Percept]) -> Action:
        """Recebe as percepções do passo atual e devolve a próxima ação.

        O agente não recebe o ambiente, apenas as pecepções locais.
        """
