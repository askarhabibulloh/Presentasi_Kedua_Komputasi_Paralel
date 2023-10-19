from PIL import Image
from multiprocessing import Process, Value


def convert_partial_grayscale(image, grayscale_image, x_start, x_end, pixels_processed):
    for x in range(x_start, x_end):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_image.putpixel((x, y), grayscale_value)

            # Update jumlah piksel yang telah diproses
            with pixels_processed.get_lock():
                pixels_processed.value += 1


if __name__ == "__main":
    input_image_path = "gambsr.jpg"
    output_image_path = "output_grayscale_image.jpg"

    image = Image.open(input_image_path)
    grayscale_image = Image.new("L", image.size)

    num_processes = 4  # Jumlah proses yang akan digunakan
    pixels_to_process = 1000000  # Batas jumlah piksel yang akan diproses

    pixels_processed = Value('i', 0)  # Jumlah piksel yang telah diproses

    processes = []
    x_range = [(i * (image.width // num_processes), (i + 1) *
                (image.width // num_processes)) for i in range(num_processes)]

    for i in range(num_processes):
        x_start, x_end = x_range[i]
        p = Process(target=convert_partial_grayscale, args=(
            image, grayscale_image, x_start, x_end, pixels_processed))
        processes.append(p)
        p.start()

    while pixels_processed.value < pixels_to_process:
        pass  # Tunggu hingga mencapai jumlah piksel yang diinginkan

    for p in processes:
        p.join()

    # Simpan gambar grayscale setelah semua proses selesai
    grayscale_image.save(output_image_path)

    # Tampilkan gambar asli dan gambar grayscale terakhir
    image.show()
    grayscale_image.show()
