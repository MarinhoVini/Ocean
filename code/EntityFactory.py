from code.Player import Player
from code.Enemy import Enemy
from code.Background import Background
from pygame import Surface, Rect

class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str):
        if entity_type == "player":
            return Player("Hero", Surface((32, 32)), Rect(0, 0, 32, 32))
        elif entity_type == "enemy":
            return Enemy("Ork", Surface((32, 32)), Rect(100, 100, 32, 32))
        elif entity_type == "bg":
            return Background("Forest", Surface((800, 600)), Rect(0, 0, 800, 600))
        return None
    