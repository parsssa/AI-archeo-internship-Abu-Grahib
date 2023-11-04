import albumentations as A
import cv2
import matplotlib.pyplot as plt



pathImage = "C:\\Users\\aweso\\Desktop\\UniBo\\2023-2024\\Tirocinio Curriculare\\AbuGrahib-2023 - Copy\\AbuGrahib\\datasets\\abu_1k\\sites\\GHR.001.jpg"
pathMask = "C:\\Users\\aweso\\Desktop\\UniBo\\2023-2024\\Tirocinio Curriculare\\AbuGrahib-2023 - Copy\\AbuGrahib\\datasets\\abu_1k\\masks\\GHR.001.png"

transform = A.Compose([
    A.RandomCrop(width=256, height=256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])


image = cv2.imread(pathImage)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mask = cv2.imread(pathMask)

transformed = transform(image=image, mask=mask)
transformed_image = transformed['image']
transformed_mask = transformed['mask']






# Create a subplot with 1 row and 2 columns
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
plt.subplot(1, 2, 1)
plt.imshow(transformed_image)
plt.axis('off')  # Turn off axis labels and ticks

plt.subplot(1, 2, 2)
plt.imshow(transformed_mask)
plt.axis('off')  # Turn off axis labels and ticks

plt.show()


