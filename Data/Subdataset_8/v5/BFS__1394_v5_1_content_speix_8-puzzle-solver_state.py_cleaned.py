from typing import Any, Optional
class State:
    def __init__(
        self,
        state: Any,
        parent: Optional['State'],
        move: Any,
        depth: int,
        cost: float,
        key: Any
    ) -> None:
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state is not None:
            self.map_str = ''.join(map(str, self.state))
    def __eq__(self, other: 'State') -> bool:
        return self.map_str == other.map_str
    def __lt__(self, other: 'State') -> bool:
        return self.map_str < other.map_str