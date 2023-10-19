import cv2
import numpy as np

# Baca gambar
gambar = cv2.imread('gambsr.jpg')

# Buat kernel stencil Von Neumann
kernel = np.array([[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]], np.uint8) / 5

# Lakukan operasi konvolusi untuk melakukan blur
hasil_blur = cv2.filter2D(gambar, -1, kernel)

# Tampilkan gambar asli dan gambar hasil blur
cv2.imshow('Gambar Asli', gambar)
cv2.imshow('Hasil Blur', hasil_blur)

# Tunggu tombol apapun ditekan dan keluar
cv2.waitKey(0)
cv2.destroyAllWindows()
