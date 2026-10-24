import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:
    """
    Returns a 2D float64 array of zeros or ones with the requested shape.
    """
    res = []
    rows = shape[0]
    columns = shape[1]
    for i in range(rows):
        if kind == "zeros":
            arr = np.zeros(columns,dtype="float64")
            res.append(arr)
    
        if kind == "ones":
            arr = np.ones(columns,dtype="float64")
            res.append(arr)

    return np.array(res)