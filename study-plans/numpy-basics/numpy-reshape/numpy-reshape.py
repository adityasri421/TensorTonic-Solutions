import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    row,column = len(data),len(data[0])
    dim = row*column
    if operation=="add_batch":
        np_array = np.array(data,dtype="float64")
        res = np_array.reshape(1,row,column)

    if operation=="flatten":
        np_array = np.array(data,dtype="float64")
        res = np_array.flatten()

    if operation=="transpose":
        np_array = np.array(data,dtype="float64")
        res = np_array.T

    return res
