import cv2

# Buka citra digital foto
image = cv2.imread("D:\Pengolahan Citra Digital\gambar.jpg") 

if image is not None:
    # Mendapatkan dimensi gambar
    height, width, channels = image.shape

    # Tampilkan dimensi gambar
    print(f'Dimensi Gambar: {width}x{height}')

    # Akses 10 nilai piksel pertama dalam bentuk RGB
    for i in range(10):
        pixel_value = image[i, 0] 
        print(f'Pixel {i+1} (RGB): {pixel_value}')
else:
    print()
