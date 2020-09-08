import glooey

from game.gui import gui


class Inventory(glooey.Widget):
    num_rows = 5
    num_cols = 5

    Grid = glooey.Grid
    Cell = glooey.Label
    

    def __init__(self, *args, **kwargs):
        super(Inventory, self).__init__(*args, **kwargs)

        self.items = [["hej!"] * self.num_rows]* self.num_cols

        # Create widgets
        self.grid = self.Grid()

        for x in range(self.num_rows):
            for y in range(self.num_cols):
                self.grid.add(x,y, self.Cell(self.items[x][y]))

        self._attach_child(self.grid)