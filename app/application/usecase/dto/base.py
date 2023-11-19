from dataclasses import dataclass


@dataclass
class Dto:
    pass


class MaskedString(str):
    def __repr__(self):
        return "*" * len(self)
