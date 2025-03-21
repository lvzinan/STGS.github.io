from PIL import Image, ImageDraw

# 读取图片
image_path = 'rubble-switch.jpg'  # 输入图片的路径
image = Image.open(image_path)

# 定义目标大小
target_size = (1600, 1200)  # 替换为您想要的大小 (宽, 高)

# 调整图片大小
image = image.resize(target_size)

# 创建一个可以在图像上绘制的对象
draw = ImageDraw.Draw(image)

# 定义矩形框的坐标 (左上角x, 左上角y, 右下角x, 右下角y)
box_coords = (4, 268, 304, 568)

# 在图像上绘制红色矩形框
draw.rectangle(box_coords, outline="red", width=5)

# 保存新的图片
output_path = 'rubble-switch1.jpg'  # 输出图片的路径
image.save(output_path)

print(f"新图片已保存到 {output_path}")