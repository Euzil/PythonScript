from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_path, output_path, watermark_text):
    # 打开图片
    image = Image.open(input_path)
    # 准备绘制对象
    draw = ImageDraw.Draw(image)
    # 设置字体（这里使用Arial，大小为36）
    font = ImageFont.truetype('arial.ttf', 36)
    # 在图片上添加水印文字
    draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)
    # 保存带有水印的图片
    image.save(output_path)

# 替换为自己的文件路径和水印文本
add_watermark('path_to_input_image.jpg', 'path_to_watermarked_image.jpg', 'Your Watermark Text')