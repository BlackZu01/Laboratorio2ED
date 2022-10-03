class Node:
    
    def __init__(self, data: str, info: list) -> None:
        self.data = data
        self.info_neighborhood = info
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}: {self.info_neighborhood}'