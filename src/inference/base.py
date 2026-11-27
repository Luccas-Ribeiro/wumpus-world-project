"""Contrato do motores de inferência.

Cada familia tem sua própria assinatura, porque as respostas são diferentes:
O lógico responde sim/não, o probabilístico responde uma probabilidade.
"""

from abc import ABC, abstractmethod
from typing import Any

from src.core.models import Position


class LogicalEngine(ABC):

    name: str

    @abstractmethod
    def entails(self, kb: Any, query: Position) -> bool:
        """True se a base implica que a célula `query` é segura."""


class ProbabilistEngine(ABC):

    name: str

    @abstractmethod
    def probability_of_pit(self, kb: Any, query: Position) -> float:
        """Probabilidade de a célula `query` conter poço, dada as evidências."""
