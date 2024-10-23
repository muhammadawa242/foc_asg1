from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def generate_random_key(image):
    # Generate a random key of the same size as the image
    width, height = image.size
    random_key = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)  # 3 channels for RGB
    return random_key


def one_image(img, random_key):
    arr = np.array(img)

    random_key_image = Image.fromarray(random_key)

    # Perform XOR operation (compute cipher)
    xor_result_cipher = np.bitwise_xor(arr, random_key)

    # Convert result back to an image
    xor_image_cipher = Image.fromarray(xor_result_cipher)

    # Display the images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.title("same random key")
    plt.imshow(random_key_image)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Image")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("XOR Result")
    plt.imshow(xor_image_cipher)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    return xor_image_cipher

def xor_images(cipher1, cipher2):
    arr1 = np.array(cipher1)
    arr2 = np.array(cipher2)

    # Perform XOR operation
    xor_result = np.bitwise_xor(arr1, arr2)

    # Convert result back to an image
    xor_image = Image.fromarray(xor_result)

    # Display the images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.title("Cipher 1")
    plt.imshow(cipher1)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Cipher 2")
    plt.imshow(cipher2)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("XOR Result")
    plt.imshow(xor_image)
    plt.axis('off')

    plt.tight_layout()
    plt.show()



image1_path = 'a.jpg'
image2_path = 'b.jpg'

img1 = Image.open(image1_path).convert('RGB')
img1 = img1.rotate(-90, expand=True)
img2 = Image.open(image2_path).convert('RGB')

random_key = generate_random_key(img1)

c1 = one_image(img1, random_key)
c2 = one_image(img2, random_key)
xor_images(c1, c2)
