class Bomb:
    batteriesAA = None
    batteriesD = None
    holders = None
    serialNumber = None
    indicatorsLit = list()
    indicatorsUnlit = list()
    plates = None
    ports = dict()

    def __init__(self, batteries: int, holders: int, serialNumber: str, unlit: list[str], lit: list[str], ports: list[str], plates: int) -> None:
        self.holders = holders
        self.serialNumber = serialNumber
        self.indicatorsLit = lit
        self.indicatorsUnlit = unlit
        self.plates = plates
        self.ports = ports
        if batteries == holders:
            self.batteriesAA = 0
            self.batteriesD = batteries
        elif batteries/2 == holders:
            self.batteriesD = 0
            self.batteriesAA = batteries
        else:
            self.batteriesD = holders - batteries % holders
            self.batteriesAA = batteries - self.batteriesD
