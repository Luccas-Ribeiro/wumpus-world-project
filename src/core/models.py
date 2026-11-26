"""Tipos básicos do mundo

Contratos imutáveis usados pelo ambiente, pelo agente e pelo GUI.
Convenção: (0, 0) no canto inferior esquerdo do mundo, onde x = coluna e y = linha
"""

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Position:
    """Cordenada de uma célula."""

    x: int
    y: int


class Direction(Enum):
    """Direção para a qual o agente está virado."""

    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Action(Enum):
    """Ações possíveis do agente."""

    FORWARD = "forward"
    TURN_LEFT = "turn_left"
    TURN_RIGHT = "turn_right"
    GRAB = "grab"
    SHOOT = "shoot"
    CLIMB = "climb"


class Percept(Enum):
    """Percepções locais recebidas pelo agente em cada passo"""

    BREEZE = "breeze"   #percepção adjacente a um poço
    STENCH = "stench"   #percepção adjacente ao Wumpus
    GLITTER = "glitter" #percepção ao haver ouro na célula pisada pelo agente
    SCREAM = "scream"   #percepção quando o Wumpus morre pela flecha
