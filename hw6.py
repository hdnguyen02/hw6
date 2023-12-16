import numpy 
import matplotlib.pyplot as pl


def read_bin(file_path, size):
  with open(file_path, 'rb') as file:
    data = numpy.fromfile(file, dtype=numpy.uint8, count=size * size)
    return numpy.reshape(data, (size, size))


def show_byte_img( x,x1, x2, x3, name):
    pl.figure(figsize=(12, 6))
    pl.subplot(2, 2, 1)
    pl.imshow(x2, cmap='gray', vmin=0, vmax=255)
    pl.axis('image')
    pl.axis('off')
    pl.title(f"({name})", fontsize=12)
    pl.subplot(2, 2, 2)
    pl.imshow(x, cmap='gray', vmin=0, vmax=255)
    pl.axis('image')
    pl.axis('off')
    pl.title(f"3x3 Median Filter ({name})", fontsize=12)
    pl.subplot(2, 2, 3)
    pl.imshow(x1, cmap='gray', vmin=0, vmax=255)
    pl.axis('image')
    pl.axis('off')
    pl.title(f"3x3 Morphological Opening ({name})", fontsize=12)
    pl.subplot(2, 2, 4)
    pl.imshow(x3, cmap='gray', vmin=0, vmax=255)
    pl.axis('image')
    pl.axis('off')
    pl.title(f"3x3 Morphological Closing ({name})", fontsize=12)
    pl.show()


def apply_filters_and_display(inumpyut_file, size, w_size, name):
    w_sizeo2 = w_size // 2

    W = numpy.zeros((w_size, w_size))
    yMF = numpy.zeros((size, size))
    yE = numpy.zeros((size, size))
    yD = numpy.zeros((size, size))
    yO = numpy.zeros((size, size))
    yC = numpy.zeros((size, size))

    x = read_bin(inumpyut_file, size)

    for row in range(w_sizeo2, size - w_sizeo2):
        for col in range(w_sizeo2, size - w_sizeo2):
            W = x[row - w_sizeo2:row + w_sizeo2 + 1, col - w_sizeo2:col + w_sizeo2 + 1]
            yMF[row, col] = numpy.median(W)
            yE[row, col] = numpy.min(W)
            yD[row, col] = numpy.max(W)

    for row in range(w_sizeo2 + 1, size - w_sizeo2 - 1):
        for col in range(w_sizeo2 + 1, size - w_sizeo2 - 1):
            W = yE[row - w_sizeo2:row + w_sizeo2 + 1, col - w_sizeo2:col + w_sizeo2 + 1]
            yO[row, col] = numpy.max(W)
            W = yD[row - w_sizeo2:row + w_sizeo2 + 1, col - w_sizeo2:col + w_sizeo2 + 1]
            yC[row, col] = numpy.min(W)

    show_byte_img(x, yMF, yO, yC, name)


apply_filters_and_display("../image/camera99bin.sec", 256, 3, 'camera99bin')
apply_filters_and_display("../image/camera9bin.sec", 256, 3, 'camera9bin')
