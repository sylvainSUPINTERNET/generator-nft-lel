from PIL import Image
import numpy as np

from random import randint


w, h = 512, 512

shrink = 210

data = np.zeros((h, w, 3), dtype=np.uint8)

def generateBlobs(w, h, data, itteration, shrink = 0):
    itteration = itteration - 1


    x1 = randint(0,(w-1))
    x2 = randint(0,(w-1))
    x3 = randint(0,(w-1))
    x4 = randint(0,(w-1))
    print(f"{x1}:{x2}, {x3}:{x4}")

    data[x1:x2, x3:x4] = [randint(1,255),randint(1,255),randint(1,255)]
    # data[
    #     randint(1,w-1):randint(1,w-1),
    #     randint(1,w-1):randint(1,w-1)] = [randint(0,255),randint(0,255),randint(0,255)]

    # data[0:256, 0:256] = [255, 48, 120] 
    # data[350:452, 350:452] = [10, 48, 120] 

    if itteration != 0:
        generateBlobs(w, h, data, itteration, shrink)
    
    return data;


result = generateBlobs(w, h, data, 800, shrink)
img = Image.fromarray(result, 'RGB')
img.save('nft_random.png')
img.show()

