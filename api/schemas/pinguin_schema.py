from pydantic import BaseModel
from typing import Optional, List
from model.pinguin import Pinguin
import json
import numpy as np

class PinguinSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "pinguin_01"
    lenght: float = 47.2
    depth: float = 13.7
    flipper: float = 214.5
    mass: float = 4925.1
    
class PinguinViewSchema(BaseModel):
    """Define como um pinguin será retornado
    """
    id: int = 1
    name: str = "pinguin_01"
    lenght: float = 47.2
    depth: float = 13.7
    flipper: float = 214.0
    mass: float = 4925.0
    outcome: str = "Adelie"
    
class PinguinBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "pinguin_01"

class ListaPinguinSchema(BaseModel):
    """Define como uma lista de pinguins será representada
    """
    pinguins: List[PinguinSchema]

    
class PinguinDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "pinguin_01"
    
# Apresenta apenas os dados de um pinguin    
def apresenta_pinguin(pinguin: Pinguin):
    """ Retorna uma representação do pinguin seguindo o schema definido em
        PinguinViewSchema.
    """
    return {
        "id": pinguin.id,
        "name": pinguin.name,
        "lenght": pinguin.lenght,
        "depth": pinguin.depth,
        "flipper": pinguin.flipper,
        "mass": pinguin.mass,
        "outcome": pinguin.outcome,
    }
    
# Apresenta uma lista de pinguins
def apresenta_pinguins(pinguins: List[Pinguin]):
    """ Retorna uma representação do pinguin seguindo o schema definido em
        PinguinViewSchema.
    """
    result = []
    for pinguin in pinguins:
        result.append({
            "id": pinguin.id,
            "name": pinguin.name,
            "lenght": pinguin.lenght,
            "depth": pinguin.depth,
            "flipper": pinguin.flipper,    
            "mass": pinguin.mass,
            "outcome": pinguin.outcome
        })

    return {"pinguins": result}

