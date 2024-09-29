class Turn:
    """
    A Turn class consisting of origins, destination coordinates, a style name and a player id.
    """
    row_o: int
    col_o: int
    row_d: int
    col_d: int
    style_name: str
    player: str

    def __init__(self, row_o: int, col_o: int, row_d: int, col_d: int, style_name: str, player: str):
        """
        Initializes a Turn class
        """
        self.row_o = row_o
        self.col_o = col_o
        self.row_d = row_d
        self.col_d = col_d
        self.style_name = style_name
        self.player = player
