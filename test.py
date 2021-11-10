from PIL import Image


def change(num):
    return int(int(num / 2))


def capture_picture(img_path):
    """
    从中间截取图片, 返回两张图片
    :param img_path: 图片地址
    :return:
    """
    read_img = Image.open(img_path)
    area = read_img.size
    length, width = area
    # crop (left, upper, right, lower) 左上，右下
    cropped_first = read_img.crop((100, 100, change(length), change(length)))
    # cropped = read_img.crop((1400, 200, 2300, 2300))
    cropped_second = read_img.crop((change(length) + 200, 200, int(length) - 200, int(length) - 200))
    cropped_first.save('c.jpg')
    cropped_second.save('b.jpg')
    return cropped_first, cropped_second


img = "安吉蓝城电子商务有限公司.jpeg"
capture_picture(img)