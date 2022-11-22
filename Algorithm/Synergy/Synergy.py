from enum import Enum

class Synergy(Enum):
    MINT_CHOCOLATE = {"SESAME_OIL": 1, "KOCHUJANG": 3, "MAYONNAISE": 7, "SOJU": 2, "CHEESE" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    SESAME_OIL = {"MINT_CHOCOLATE": 2, "KOCHUJANG": 4, "MAYONNAISE": 7, "SOJU": 8, "CHEESE" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    KOCHUJANG = {"MINT_CHOCOLATE": 3, "SESAME_OIL": 7, "MAYONNAISE": 7, "SOJU": 2, "CHEESE" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    MAYONNAISE = {"MINT_CHOCOLATE": 3, "SESAME_OIL": 5, "KOCHUJANG": 4, "SOJU": 2, "CHEESE" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    SOJU = {"MINT_CHOCOLATE": 2, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "CHEESE" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    CHEESE = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "SOJU" : 4, "GALIC" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    GALIC = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "SOJU" : 4, "CHEESE" : 5, "ONION" : 6, "JUICE" : 8, "WATER" : 3}
    ONION = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "SOJU" : 4, "CHEESE" : 5, "GALIC" : 6, "JUICE" : 8, "WATER" : 3}
    JUICE = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "SOJU" : 4, "CHEESE" : 5, "GALIC" : 6, "ONION" : 8, "WATER" : 3}
    WATER = {"MINT_CHOCOLATE": 1, "SESAME_OIL": 3, "KOCHUJANG": 7, "MAYONNAISE": 2, "SOJU" : 4, "CHEESE" : 5, "GALIC" : 6, "ONION" : 8, "JUICE" : 3}
    
    def getSynergyList():
        return ['MINT_CHOCOLATE', 'SESAME_OIL', 'KOCHUJANG', 'MAYONNAISE', 'SOJU', 'CHEESE', 'GALIC', 'ONION', 'JUICE', 'WATER']
    
# 민트초코, 참기름, 고추장, 마요네즈, 소주, 치즈, 마늘, 양파, 주스, 물