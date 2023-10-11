import sys

red = int(sys.argv[1])
green = int(sys.argv[2])
blue = int(sys.argv[3])


grayscale = (red + green + blue)/3
print(grayscale)
