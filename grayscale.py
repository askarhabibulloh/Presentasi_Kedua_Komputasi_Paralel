from PIL import Image

input_image_path = "gambsr.jpg"
output_image_path = "hasil/output_grayscale_image.jpg"

image = Image.open(input_image_path)
grayscale_image = Image.new("L", image.size)

for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_image.putpixel((x, y), grayscale_value)

        if (x * image.width + y) % 1000000 == 0:
            partial_output_path = f"output_partial_grayscale_{x * image.width + y}.jpg"
            grayscale_image.save(partial_output_path)
            grayscale_image.show()

# Simpan gambar grayscale setelah loop selesai
grayscale_image.save(output_image_path)

# Tampilkan gambar grayscale terakhir
grayscale_image.show()
