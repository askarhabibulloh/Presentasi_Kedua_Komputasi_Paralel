from PIL import Image

input_image_path = "gambsr.jpg"
output_image_path = "output_grayscale_image.jpg"

image = Image.open(input_image_path)
grayscale_image = Image.new("L", image.size)

for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_image.putpixel((x, y), grayscale_value)

grayscale_image.save(output_image_path)

image.show()
grayscale_image.show()
