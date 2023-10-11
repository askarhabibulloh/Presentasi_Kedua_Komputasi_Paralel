import sys

red = int(sys.argv[1])
green = int(sys.argv[2])
blue = int(sys.argv[3])


grayscale = 0.299*red + 0.587*green + 0.114*blue
print(grayscale)
