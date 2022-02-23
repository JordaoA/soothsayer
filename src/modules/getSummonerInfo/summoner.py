"""
Codigo responsavel por coletar infromações do jogador.
"""
from dataclasses import dataclass

@dataclass
class Summoner:
    id_: str
    name: str
    accountId: str
    puuid: str
    profileIconId: int
    summonerLevel: int
        