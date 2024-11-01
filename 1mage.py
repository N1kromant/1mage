from PIL import Image
import numpy as np
restored_array = np.fromfile("data.dat", dtype=np.uint8).reshape(-1, 3)
restored_images = [restored_array[i::5].reshape(1000, 1000, 3) for i in range(5)]

def uno():
    image_to_show = Image.fromarray(restored_array[0::5].reshape(1000, 1000, 3))
    image_to_show.show()
def dos():
    image_to_show = Image.fromarray(restored_array[1::5].reshape(1000, 1000, 3))
    image_to_show.show()
def tres():
    image_to_show = Image.fromarray(restored_array[2::5].reshape(1000, 1000, 3))
    image_to_show.show()
def cuatro():
    image_to_show = Image.fromarray(restored_array[3::5].reshape(1000, 1000, 3))
    image_to_show.show()
def cinco():
    image_to_show = Image.fromarray(restored_array[4::5].reshape(1000, 1000, 3))
    image_to_show.show()

uno()
