import numpy.typing as npt


def add_safely(arr1: npt.NDArray, arr2: npt.NDArray):
    (longer, shorter) = (arr2, arr1) if len(arr1) < len(arr2) else (arr1, arr2)
    result = longer.copy()
    result[:len(shorter)] += shorter
    return result
