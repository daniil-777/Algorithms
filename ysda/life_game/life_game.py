import copy


class LifeGame(object):
    """
    Class for Game life
    """
    def __init__(self, ocean=[]):
        self.ocean = ocean
        self.raws = len(ocean)
        if self.raws:
            self.columns = len(ocean[0])
        else:
            self.columns = 0
        self.new_gen = ocean

    def get_next_generation(self):
        if self.columns == 0 or self.raws == 0:
            return self.ocean
        self._new_horizont()

        wr = copy.deepcopy(self.new_gen)
        for l in range(self.raws + 2):
            for c in range(self.columns + 2):
                wr[l][c] = self._next_gen_for_item(l, c)

        self.ocean = copy.deepcopy(self._cut_the_map(wr))
        return self.ocean

    def _next_gen_for_item(self, raw, column):

        if self.new_gen[raw][column] == 1:
            return 1
        elif self.new_gen[raw][column] == 0\
                and self._get_count_neighbours(raw, column, 2) == 3:
            return 2
        elif self.new_gen[raw][column] == 0 \
                and self._get_count_neighbours(raw, column, 3) == 3:
            return 3
        elif self.new_gen[raw][column] == 2 \
                and self._get_count_neighbours(raw, column, 2) > 3:
            return 0
        elif self.new_gen[raw][column] == 2 \
                and self._get_count_neighbours(raw, column, 2) < 2:
            return 0
        elif self.new_gen[raw][column] == 3 \
                and self._get_count_neighbours(raw, column, 3) > 3:
            return 0
        elif self.new_gen[raw][column] == 3 \
                and self._get_count_neighbours(raw, column, 3) < 2:
            return 0
        else:
            return self.new_gen[raw][column]

    def _assert_on_squareect(self, raw, column, square, neighb):
        if square == 0:
            if raw > 0 and column > 0:
                return int(self.new_gen[raw - 1][column - 1] == neighb)
            else:
                return 0
        elif square == 1:
            if raw > 0:
                return int(self.new_gen[raw - 1][column] == neighb)
            else:
                return 0
        elif square == 2:
            if raw > 0 and column < self.columns + 1:
                return int(self.new_gen[raw - 1][column + 1] == neighb)
            else:
                return 0
        elif square == 3:
            if column > 0:
                return int(self.new_gen[raw][column - 1] == neighb)
            else:
                return 0
        elif square == 4:
            if column < self.columns + 1:
                return int(self.new_gen[raw][column + 1] == neighb)
            else:
                return 0
        elif square == 5:
            if raw < self.raws + 1 and column > 0:
                return int(self.new_gen[raw
                                        + 1][column - 1] == neighb)
            else:
                return 0
        elif square == 6:
            if raw < self.raws + 1:
                return int(self.new_gen[raw + 1][column] == neighb)
            else:
                return 0
        elif square == 7:
            if raw < (self.raws + 1) and column < (self.columns + 1):
                return int(self.new_gen[raw
                                        + 1][column + 1] == neighb)
            else:
                return 0

    def _get_count_neighbours(self, raw, column, neighb):
        res = 0
        for square in range(8):
            res += self._assert_on_squareect(raw, column, square, neighb)
        return res

    def _cut_the_map(self, new_large_map):
        new_large_map = self._cut_up(new_large_map)
        new_large_map = self._cut_left(new_large_map)
        new_large_map = self._cut_right(new_large_map)
        new_large_map = self._cut_down(new_large_map)
        if self.columns + 1 < len(new_large_map[0]):
            new_large_map = self._cut_left(new_large_map)
        if self.columns + 1 < len(new_large_map[0]):
            new_large_map = self._cut_right(new_large_map)
        if self.raws + 1 < len(new_large_map):
            new_large_map = self._cut_up(new_large_map)
        if self.raws + 1 < len(new_large_map):
            new_large_map = self._cut_down(new_large_map)

        self.columns = len(new_large_map[0])
        self.raws = len(new_large_map)

        return new_large_map

    def _cut_up(self, map):
        raws = len(map)
        for i in range(raws - 1):
            map[i] = map[i + 1]
        map.pop()
        return map

    def _cut_left(self, map):
        raws = len(map)
        columns = len(map[0])
        for i in range(raws):
            for j in range(columns - 1):
                map[i][j] = map[i][j + 1]
        for j in range(raws):
            map[j].pop()
        return map

    def _cut_right(self, map):
        raws = len(map)
        for j in range(raws):
            map[j].pop()
        return map

    def _cut_down(self, map):
        map.pop()
        return map

    def _new_horizont(self):
        self.new_gen = [[0]*(self.columns + 2)]
        for l in range(len(self.ocean)):
                self.new_gen.append([0] + self.ocean[l] + [0])
        self.new_gen.append([0] * (self.columns + 2))
