"""Contrato da base de conhecimento.

O agente só conhece essa interface, então trocar LogicalKB por ProbabilisticKB não exige mudar o agente.

O tipo do retorno de `ask` depende da KB:
- LogicalKB: bool (a célula é provadamente segura?)
- ProbabilisticKB: float entre 0 e 1 (probabilidade de poço)
"""

from abc import ABC, abstractmethod

from src.core.models import Percept, Position


class KnowledgeBase[R](ABC):
    """Base de conhecimento com TELL e ASK."""

    @abstractmethod
    def tell(self, position: Position, percepts: list[Percept]) -> None:
        """Registra as percepções recebidas na posição atual.

        Traduz as percepções em conhecimento sobre as células vizinhas.
        """


    @abstractmethod
    def ask(self, position: Position) -> R:
        """Consulta a base sobre a célular `position`

        Retorno definido pela subclasse
        """


    @abstractmethod
    def reset(self) -> None:
        """Descarta todo o conhecimento da KB"""
