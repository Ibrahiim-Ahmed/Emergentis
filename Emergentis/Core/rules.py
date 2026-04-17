class Rules:
    """
    Defines rules for cellular automata.
    You can extend this for different systems.
    """

    @staticmethod
    def conway(cell, neighbors):
        # ITERATIVE RULE APPLICATION
        if cell == 1 and neighbors in [2, 3]:
            return 1
        if cell == 0 and neighbors == 3:
            return 1
        return 0