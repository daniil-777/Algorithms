class Player(object):
    def play(self, game):
        """
        :param game: some class with method start
        """


def play(game):
    p = Player()
    for i in range(1000000):
        p.play(game)
