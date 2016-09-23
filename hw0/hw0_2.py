from PIL import Image
import sys

fileName = sys.argv[1]

im = Image.open(fileName)

im = im.transpose(Image.FLIP_LEFT_RIGHT)
im = im.transpose(Image.FLIP_TOP_BOTTOM)

im.save('ans2.png')
