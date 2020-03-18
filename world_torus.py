from cell import Cell
import random
from world import World

class World_Torus(World):

    def create_neighbors(self):
        """
        Loop through the grid and assign the neighbors to each cell.
        :return: None
        """
        # print('---creating neighbors---')
        for row in self._grid:
            for cell in row:
                    #
                    # There are some nine situations that we have to account for:
                    #
                    # 1. upper left corner (3 neighbors)
                    # 2. rest of the top row (5 neighbors)
                    # 3. upper right corner (3 neighbors)
                    # 4. far left side (5 neighbors)
                    # 5. normal cells (8 neighbors)
                    # 6. far right side (5 neighbors)
                    # 7. lower left corner (3 neighbors)
                    # 8. rest of bottom row (5 neighbors)
                    # 9. lower right corner (3 neighbors)
                    #
                row = cell.get_row()
                column = cell.get_column()
                    # print(f'({row},{column})')
                    # top row
                if row == 0:
                        # 1. upper left corner (3 neighbors)
                    if column == 0:
                            # print('upper left')
                        cell.add_neighbor(self._grid[self._rows - 1][column + 1])
                        cell.add_neighbor(self._grid[self._rows - 1][self._columns - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row][self._columns - 1])
                        cell.add_neighbor(self._grid[row + 1][self._columns - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        # 2. rest of the top row (5 neighbors)
                    elif column < (self._columns - 1):
                        # print('upper row')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column])
                        cell.add_neighbor(self._grid[self._rows - 1][column - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column + 1])
                        # 3. upper right corner (3 neighbors)
                    else:
                            # print('upper right')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][0])
                        cell.add_neighbor(self._grid[row][0])
                        cell.add_neighbor(self._grid[self._rows - 1][0])
                        cell.add_neighbor(self._grid[self._rows - 1][column])
                        cell.add_neighbor(self._grid[self._rows - 1][column - 1])

                    # middle row
                elif row < (self._rows - 1):
                        # 4. far left side (5 neighbors)
                    if column == 0:
                            # print('left side')
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        cell.add_neighbor(self._grid[row][self._columns - 1])
                        cell.add_neighbor(self._grid[row - 1][self._columns - 1])
                        cell.add_neighbor(self._grid[row + 1][self._columns - 1])
                        # 5. normal cells (8 neighbors)
                    elif column < (self._columns - 1):
                            # print('middle')
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        # 6. far right side (5 neighbors)
                    else:
                            # print('right side')
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row][0])
                        cell.add_neighbor(self._grid[row + 1][0])
                        cell.add_neighbor(self._grid[row - 1][0])
                    # bottom row
                else:
                        # 7. lower left corner (3 neighbors)
                    if column == 0:
                            # print('lower left')
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[0][column + 1])
                        cell.add_neighbor(self._grid[0][column])
                        cell.add_neighbor(self._grid[0][self._columns - 1])
                        cell.add_neighbor(self._grid[row][self._columns - 1])
                        cell.add_neighbor(self._grid[row - 1][self._columns - 1])
                        # 8. rest of the bottom row (5 neighbors)
                    elif column < (self._columns - 1):
                            # print('lower row')
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[0][column])
                        cell.add_neighbor(self._grid[0][column + 1])
                        cell.add_neighbor(self._grid[0][column - 1])
                        # 9. lower right corner (3 neighbors)
                    else:
                            # print('lower right')
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[0][column - 1])
                        cell.add_neighbor(self._grid[0][column])
                        cell.add_neighbor(self._grid[0][0])
                        cell.add_neighbor(self._grid[row][0])
                        cell.add_neighbor(self._grid[row - 1][0])

