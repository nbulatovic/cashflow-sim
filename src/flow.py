from typing import List, Union

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


class Flow:

    def __init__(self, amounts: Union[List | npt.NDArray]):
        self._data = np.array(amounts, dtype=np.int64)
        if len(self._data.shape) != 1:
            raise ValueError("A Flow is one dimensional")

    def __len__(self):
        return len(self._data)

    def __eq__(self, other):
        return np.array_equal(self._data, other._data)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError(
                f"Sizes don't match: {len(self)} != {len(other)}")
        return Flow(np.add(self._data, other._data))

    def __str__(self):
        return f'{type(self).__name__}({self._data})'

    def __repr__(self):
        return self.__str__()

    def total(self):
        return self._data.sum()

    def merge(self, flows):
        merged = self
        for flow in flows:
            merged += flow
        return merged

    def update(self, other):
        self._data = np.add(self._data, other._data)

    def is_negative(self, include_zero=False):
        if include_zero:
            return np.all(self._data <= 0)
        return np.all(self._data < 0)

    def is_positive(self, include_zero=False):
        if include_zero:
            return np.all(self._data >= 0)
        return np.all(self._data > 0)

    def plot(self):
        x = np.arange(len(self._data))
        y = self._data
        color = np.where(y < 0, "r", "g")

        plt.figure(figsize=(12, 4), dpi=100)
        plt.bar(x, y, color=color)
        plt.tight_layout()
        plt.show()
