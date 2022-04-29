from aip import AipOcr
from PIL import Image


def capture_picture(img):
    """
    从中间截取图片, 返回两张图片
    :param img: 图片地址
    :return:
    """
    read_img = Image.open(img)
    area = read_img.size
    length, width = area
    # crop (left, upper, right, lower) 左上，右下
    cropped_first = read_img.crop((100, 100, change(length), change(length)))
    # cropped = read_img.crop((1400, 200, 2300, 2300))
    cropped_second = read_img.crop((change(length) + 200, 200, int(length) - 200, int(length) - 200))
    cropped_first.save('c.jpg')
    cropped_second.save('b.jpg')
    return cropped_first, cropped_second


def change(num):
    return int(int(num / 2))


def baidu_recognition(img_paths):
    """
    百度api执行所需数据，运行需换成自己的APP_ID，API_KEY，SECRET_KEY
    :param img_paths: 图片地址
    :return:
    """
    app_id = ''
    api_key = ''
    secret_key = ''
    # 初始化AipOcr
    aip_ocr = AipOcr(app_id, api_key, secret_key)
    # with open(img_paths, 'rb') as f:
    #     img2 = f.read()
    # print(type(img2))
    # 识别图片并返回结果
    result = aip_ocr.basicAccurate(img_paths)
    return result


def parse_picture(binary_data):
    """
    解析识别的翻译文本
    :param binary_data:
    :return:
    """
    words_result = binary_data["words_result"]
    print(words_result)
    # for data in words_result:
    #     print(data)


if __name__ == '__main__':
    # img_path = r'C:\Users\Administrator\Desktop\营业执照\苍南县翎翎电子商务有限公司.jpeg'
    img_path = r'安吉蓝城电子商务有限公司.jpeg'
    a, b = capture_picture(img_path)
    binary = baidu_recognition(a)
    parse_picture(binary)
    binary = baidu_recognition(b)
    parse_picture(binary)


