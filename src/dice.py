import random
from typing import List

def roll_dice(sides: int = 6) -> int:
    """Retorna um número aleatório de 1..sides."""
    if not isinstance(sides, int) or sides < 2:
        raise ValueError("sides deve ser inteiro >= 2")
    return random.randint(1, sides)

def roll_many(qty: int = 2, sides: int = 6) -> List[int]:
    """Rola 'qty' dados e retorna a lista de resultados."""
    if not isinstance(qty, int) or qty < 1:
        raise ValueError("qty deve ser inteiro >= 1")
    return [roll_dice(sides) for _ in range(qty)]

if __name__ == "__main__":
    # Smoke test rápido
    print("Um d6:", roll_dice())
    print("Três d6:", roll_many(3))
