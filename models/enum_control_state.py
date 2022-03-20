from enum import Enum, auto

class ControlState(Enum):
    AUTOMATIQUE = auto()
    MANUEL = auto()
    OUVRIR_PORTE = auto()
    FERMER_PORTE = auto()