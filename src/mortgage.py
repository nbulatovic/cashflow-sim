import numpy as np

from src.flow import Flow


class MortgageFlow(Flow):

    @classmethod
    def fixed_rate(cls, term: int, price: int):
        arr = np.full((term,), price)
        return MortgageFlow(arr)
