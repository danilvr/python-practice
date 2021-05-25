import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def dither(image):
    result = np.copy(image)

    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            pixel = result[y][x]

            new_pixel_color = round(pixel / 255) * 255
            result[y][x] = new_pixel_color
            error = pixel - new_pixel_color

            result[y][x + 1] += 7 / 16 * error
            result[y + 1][x + 1] += 1 / 16 * error
            result[y + 1][x] += 5 / 16 * error
            result[y + 1][x - 1] += 3 / 16 * error

    return result


img = np.array(cv.cvtColor(cv.imread("dither.jpeg"), cv.COLOR_BGR2GRAY), dtype=int)
plt.imshow(dither(img), cmap="gray")
plt.show()
