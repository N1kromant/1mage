from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Загружаем изображения и преобразуем их в массивы
filenames = ['images/11.png', 'images/22.png', 'images/33.png', 'images/44.png', 'images/55.png']  # Используем ваши имена файлов
images = [np.array(Image.open(file).convert('RGB')) for file in filenames]  # Конвертируем в RGB

# Проверяем, что изображения имеют размер 1000x1000
assert all(img.shape[:2] == (1000, 1000) for img in images), "Images must be 1000x1000 pixels."

# 2. Формируем объединённый массив в требуемом порядке
pixel_count = images[0].shape[0] * images[0].shape[1]  # Количество пикселей в изображении
combined_array = np.zeros((pixel_count * 5, 3), dtype=np.uint8)  # Новый массив для всех пикселей

# Распределяем пиксели по массиву
for i in range(pixel_count):
    for j in range(5):
        # Извлекаем пиксель из изображения j
        pixel = images[j][i // 1000, i % 1000]  # Берем координаты пикселя
        combined_array[i * 5 + j] = pixel

# 3. Сохраняем объединённый массив в файл
combined_array.tofile("data.dat")

# 4. Читаем объединённый массив из файла и восстанавливаем изображения
#restored_array = np.fromfile("data.dat", dtype=np.uint8).reshape(-1, 3)
#restored_images = [restored_array[i::5].reshape(1000, 1000, 3) for i in range(5)]

## 5. Функции для отображения каждого изображения
#def show_image(image_array, title="Image"):
#    plt.imshow(image_array)
#    plt.axis("off")
#    plt.title(title)
#    plt.show()

## Вызов функций для вывода изображений на экран
#for i in range(5):
#    show_image(restored_images[i], title=f"Restored Image {i + 1}")