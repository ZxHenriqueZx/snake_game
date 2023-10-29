class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        board = [
            ['+', '-', '-', '+'],
            ['|', ' ', ' ', '|'],
            ['|', ' ', ' ', '|'],
            ['|', ' ', ' ', '|'],
            ['|', ' ', ' ', '|'],
            ['|', ' ', ' ', '|'],
            ['+', '-', '-', '+'],
        ]
        return board 

    def render(self):
        matrix = self.board_matrix()

        for row in matrix:
            print(*row)
