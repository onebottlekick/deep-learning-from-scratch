gpu_enable = True

try:
    import cupy
    np = cupy
    print('GPU computation available. Using GPU')
except ImportError:
    gpu_enable = False
    import numpy
    np = numpy
    print('GPU computation not available. Using CPU')