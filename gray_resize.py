import imageio
import glob
import cv2
import numpy as np

dir = ['00000','01000','02000','00000F','01000F','02000F']
for directory in dir:
    for fname in glob.glob(directory + '/*.jpg'):
        print(fname)
        try:
            pic = imageio.imread(fname)
            # Grayscale
            pic = np.dot(pic[...,:3], [0.2989, 0.5870, 0.1140])
            # resize
            pic = cv2.resize(pic, dsize=(150, 150), interpolation=cv2.INTER_NEAREST)
            # Gaussian Blur for smoothing
            pic = cv2.GaussianBlur(pic, (5,5),0)
            # Morphology to close up holes in images
            pic = cv2.morphologyEx(pic, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
            # resave
            imageio.imwrite(directory + "-new/" + fname[7:], pic.astype(np.uint8))
        except Exception as e:
            print(fname)
            print(e)
            continue