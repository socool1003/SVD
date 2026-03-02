import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 加载图片
def load_image(image_path):
    img_obj = Image.open(image_path)

    # 转换为灰度图
    img_gray = img_obj.convert('L')

    # 转换为numpy数组
    img_matrix = np.array(img_gray)

    return img_matrix

# 测试
filename = 'cameraman.tif'

try:
    matrix = load_image(filename)

    print(f'矩阵形状：{matrix.shape}')

    plt.figure(figsize=(6, 6))
    plt.imshow(matrix, cmap='gray')
    plt.title('原始灰度图像')
    plt.axis('off')
    plt.show()

except FileNotFoundError:
    print(f'找不到文件{filename}, 请检查文件名或路径。')