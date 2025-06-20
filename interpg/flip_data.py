import numpy


def flip_data(interp_x: bool, is3d: bool, o_dims: tuple, data_t: numpy.ndarray) -> numpy.ndarray:

    """
    Flip 2D or 3D data
    args...
        interp_x: Boolean indicating x axis to be flipped (otherwise y)
        is3d: Boolean indicating data_t is 3D (otherwise 2D)
        o_dims: original data dimensions
        data_t: 2D or 3D NumPy array of data for flipping
    returns...
        data_t: 2D or 3D NumPy array of flipped data
    """

    if interp_x:
        if is3d:
            for axi in range(o_dims[0]):
                data_t[axi] = numpy.fliplr(data_t[axi])
        else:
            data_t = numpy.fliplr(data_t)
    else:
        if is3d:
            for axi in range(o_dims[0]):
                data_t[axi] = numpy.flipud(data_t[axi])
        else:
            data_t = numpy.flipud(data_t)

    return data_t
