import os

from PIL import Image

# 获取文件夹下的的jpg、png文件
def get_image_list(folderPath):
    image_list=[]
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            if file.endswith(('.jpg','.png')):
                image_list.append(os.path.join(root,file))
    return image_list

# 图片转化为icon文件
def convertToIcon(image):
    # 判断文件夹是否存在，不存在则创建
    if(bool(1-os.path.exists('convert-icon'))):
        os.makedirs('convert-icon')

    img=Image.open(image)
    img.save('convert-icon\\{0}.ico'.format(image.split('\\')[-1][:-4]))

if __name__=='__main__':
    image_list=get_image_list(os.getcwd())
    for image in image_list:
        convertToIcon(image)
