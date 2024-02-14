# Curricular Internship Project on Computer Science Applied to Archaeology
Seyed Parsa Bagheri, Jishan Rahman, Massimo Andrés Camacho
November 2023

![283512](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/c73f4e37-169b-40a2-af0a-5a50fdd9f90d)
Image: Starry Sky over the Ruins of Iraq - Credit: Hussain Diyala


## 1 Introduction
This continuation of the Baghdad-AI research project, conducted by students Seyed Parsa Bagheri, Massimo Andrés Camacho, and Jishan Rahman from the University of Bologna, fits into a long-standing context dedicated to the application of Artificial Intelligence (AI) in the field of archaeology, particularly in the area of remote sensing procedures. The original research paper by professors Marco Roccetti and Nicolò Marchetti had demonstrated the effectiveness of neural networks enhanced with segmentation mechanisms in detecting new archaeological sites in the Mesopotamian plain, integrating with traditional methodologies of archaeologists. The main goal of this internship was to engineer techniques for Data Augmentation and prevent overfitting of the model.


## 2 Work Areas
The work plan involved the augmentation of CORONA images to better train the segmentation model, contributing to a more reliable performance in predicting and identifying archaeological sites. The "Negative Sampling" phase was introduced as an additional procedure to refine the accuracy of the model. The intention was to create a complementary database containing only negative samples, allowing the model to learn from situations where the archaeological site was not present. This approach was adopted to enrich the training experience of the model, which until that point had only examined positive site-mask pairs.


## 3 Data Augmentation
Several augmented datasets were created, each using a different transformation technique from a pool of approximately 15 selected techniques (more on the selection in the following paragraph). Team members divided the techniques among themselves. Each member ran the model on Colab ten times for their assigned technique, selecting the best result to report in their individual reports. The choice of techniques referred to the academic paper "Image Data Augmentation for Deep Learning: A Survey" by Suorong Yang et al. (link to the paper), highlighting the gap in theoretical research on augmentation. After examining the taxonomy of existing augmentation methodologies, we decided to focus on the "Basic Image Manipulations" family. This decision was guided by an assessment of the tools available, primarily the Albumentations library.
![grid](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/12aa2f13-159f-4b0a-90ed-baa94071398f)

## 4 Negative Sampling
The "Negative Sampling" phase was an additional procedure to improve the model's accuracy in detecting archaeological tells. The goal was to create a database containing only negative samples to better train the model, which until that point had only examined positive site-mask pairs. Using QGIS, we worked on a map of the Baghdad area with a metric coordinate system. The map already contained points with the coordinates of archaeological tells.
![Screenshot (159)](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/0d456822-fb84-4fd4-bc23-95549de2f3bb)

Functions implemented in the QGIS UI allowed us to manually trace a "Boundaries" layer to remove unnecessary parts of the map (deserts, rivers). Subsequently, using symmetric difference, tells were removed from the boundaries. The resulting layer was saved as "Difference."
![Screenshot (158)](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/bbe5c43c-bd28-4de6-8a42-67e5d5b29e05)

![Screenshot 2023-11-24 180634](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/5a99b03f-c6f4-4db8-85e0-d4c40604bd9a)

The centroid calculation tool in QGIS was used to divide the "Difference" layer into 1000-meter side squares, capturing the x and y coordinates of each centroid. To ensure maximum precision, any intersections of centroids with tells were eliminated through a Python script. Finally, the "Negative Sampling" step was completed by exporting the centroids to a CSV dataset. Using this dataset and the QGIS console, a Python script was applied to crop and export the necessary images, obtaining the input for the subsequent model training phase.
![Screenshot (160)](https://github.com/parsssa/AI-archeo-tirocinio-Abu-Grahib/assets/107321532/52f64e9d-a1e1-4139-932e-c1e88c6ee998)


## 5 Final Considerations
Our project highlighted the effectiveness of data augmentation techniques and Negative Sampling in discriminating archaeological sites through CORONA satellite images. Despite the limited computational power, due to the exclusive use of Google Colab instead of a dedicated server, we managed to achieve promising results. This limitation forced the team to optimize algorithms and be selective in choosing augmentation techniques, balancing data quality and quantity.

The use of QGIS for Negative Sampling ensured high geographic precision, contributing to strengthening the accuracy of our model. The adopted methodology, focused on both positive and negative samples, demonstrated a tangible improvement in the model's ability to correctly distinguish areas of interest.

The selection of augmentation techniques was guided by an in-depth theoretical and practical analysis, focusing on basic manipulations suitable for grayscale images. This approach effectively expanded the dataset without compromising its quality.

In conclusion, despite the challenges posed by limited computational power, the project provided valuable insights into how targeted application of data augmentation and Negative Sampling can significantly improve the performance of machine learning models in archaeological contexts. These findings open new perspectives for future research, suggesting that such methodologies can be effectively employed even with limited computational resources.
