from typing import List, Union

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


class Flow:
    def __init__(self, arr: Union[List | npt.NDArray]):
        self._arr = np.array(arr, dtype=np.int64)
        if len(self._arr.shape) != 1:
            raise ValueError("A Flow is one dimensional")

    def __len__(self):
        return len(self._arr)

    def __eq__(self, other):
        return np.array_equal(self._arr, other._arr)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError(
                f"Sizes don't match: {len(self)} != {len(other)}")
        return Flow(np.add(self._arr, other._arr))

    def __str__(self):
        return f'{type(self).__name__}({self._arr})'

    def __repr__(self):
        return self.__str__()

    def total(self):
        return self._arr.sum()

    def merge(self, flows):
        merged = self
        for flow in flows:
            merged += flow
        return merged

    def plot(self):
        x = np.arange(len(self._arr))
        y = self._arr
        color = np.where(y < 0, "r", "g")

        plt.figure(figsize=(12, 4), dpi=100)
        plt.bar(x, y, color=color)
        plt.tight_layout()
        plt.show()
