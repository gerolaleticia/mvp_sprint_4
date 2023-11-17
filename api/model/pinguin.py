from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g

class Pinguin(Base):
    __tablename__ = 'pinguins'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    lenght = Column("culmen_length_mm", Float)
    depth = Column("culmen_depth_mm", Float)
    flipper = Column("flipper_length_mm", Float)
    mass = Column("body_mass_g", Float)
    outcome = Column("species", String(50))
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, lenght:float, depth:float, flipper:float, name:str, mass:float, 
                 outcome: str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Pinguin

        Arguments:
            name: identificador do pinguin
            lenght: comprimento culmen
            depth: largura culmen        
            flipper: comprimento asa        
            mass: índice de massa corporal        
            outcome: espécie        
            data_insercao: data de quando o pinguin foi inserido à base        
        """
        self.name=name
        self.lenght = lenght
        self.depth = depth
        self.flipper = flipper
        self.mass = mass
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao