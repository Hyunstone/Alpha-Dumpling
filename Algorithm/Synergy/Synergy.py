from enum import Enum

class Synergy(Enum):
    APPLE = {"BANANA": 1, "COKE": 3, "GUN": 7, "COCAINE": 2}
    COCAINE = {"APPLE": 2, "COKE": 4, "BANANA": 7, "GUN": 8}
    BANANA = {"APPLE": 3, "COCAINE": 7, "COKE": 4, "GUN": 1}
    COKE = {"APPLE": 3, "COCAINE": 5, "BANANA": 4, "GUN": 3}
    GUN = {"COCAINE": 2, "BANANA": 1, "COKE": 3, "APPLE": 0}
    
    def getSynergyList():
        return ['APPLE', 'COCAINE', 'BANANA', 'COKE', 'GUN']