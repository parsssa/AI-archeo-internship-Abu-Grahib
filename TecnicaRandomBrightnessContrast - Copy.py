import cv2
from matplotlib import pyplot as plt
from albumentations import RandomBrightnessContrast

# Percorsi delle immagini
img_path1 = "/path/to/your/image1.jpg"
img_path2 = "/path/to/your/image2.jpg"
img_path3 = "/path/to/your/image3.jpg"

# Carica le immagini
img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)
img3 = cv2.imread(img_path3)

# Crea una lista delle immagini
images = [img1, img2, img3]

# Applica la trasformazione RandomBrightnessContrast
transform = RandomBrightnessContrast()
transformed_images = [transform(image=image)['image'] for image in images]

# Plotta le immagini
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

for i, img in enumerate(images):
    axs[0, i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[0, i].set_title('Before')
    axs[0, i].axis('off')

for i, img in enumerate(transformed_images):
    axs[1, i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[1, i].set_title('After')
    axs[1, i].axis('off')

plt.show()