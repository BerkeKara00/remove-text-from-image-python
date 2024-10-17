import matplotlib.pyplot as plt
import keras_ocr
import cv2
import numpy as np


# Orta noktaları bularak kullanıcının girdiği ölçekleme değerine göre poligonu oluşturuyoruz.
def expand_polygon(polygon, scale=1.2):
    cx = np.mean(polygon[:, 0])
    cy = np.mean(polygon[:, 1])

    new_polygon = np.array([[cx + scale * (x - cx), cy + scale * (y - cy)] for (x, y) in polygon])

    return new_polygon.astype(np.int32)


def indexleri_maskele(img_path, pipeline, word_indices=[], scale=1.2):
    img = keras_ocr.tools.read(img_path)
    prediction_groups = pipeline.recognize([img])

    mask = np.zeros(img.shape[:2], dtype="uint8")

    # -1 değeri girilince bütün indeksleri seçiyoruz.
    if -1 in word_indices:
        word_indices = list(range(len(prediction_groups[0])))

    for word_index in word_indices:

        if len(prediction_groups[0]) > word_index:
            selected_word = prediction_groups[0][word_index]

            #seçilen kelimelerin köşe noktaları seçilerek poligonlara maskeleme işlemi yapılıyor.
            polygon = np.array([selected_word[1][0], selected_word[1][1], selected_word[1][2], selected_word[1][3]])

            expanded_polygon = expand_polygon(polygon, scale=scale)

            cv2.fillPoly(mask, [expanded_polygon], 255)

    inpainted_img = cv2.inpaint(img, mask, 7, cv2.INPAINT_TELEA)

    return inpainted_img


#keras-ocr modeli görseldeki kelimeleri tespit ediyoruz.
pipeline = keras_ocr.pipeline.Pipeline()

#Kullanıcıdan dinamik şekilde index ve ölçekleme bilgilerini alıyoruz.
indices_input = input("Index girin (tümünü silmek için -1'e basın) --> ")
word_indices = list(map(int, indices_input.split(',')))

scale = float(input("Maskeleme alanını genişletin :  (Örn : 1, 1.1 , 1.2)--> "))

img_text_removed = indexleri_maskele('data/3.jpg', pipeline, word_indices=word_indices, scale=scale)


img_text_removed_bgr = cv2.cvtColor(img_text_removed, cv2.COLOR_RGB2BGR)


#Sonucu output klasörüne kaydediyoruz.
cv2.imwrite('output/masked_image.jpg', img_text_removed_bgr)

# Görselleştirme
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(keras_ocr.tools.read('data/3.jpg'))
axs[0].set_title('Orijinal')
axs[1].imshow(img_text_removed)
axs[1].set_title('Maske Sonrası')
for ax in axs:
    ax.axis('off')
plt.show()
