import os
import os.path
from PIL import Image

def covertImage():
    print("start covert image")
    print("请输入图片所在文件夹")
    print("attention: 程序会转换当前文件夹下的所有符合条件的图片")
    dirPath = input()
    imageFileList = os.listdir(dirPath)
    for file in imageFileList:
        filePath = os.path.join(dirPath, file)
        if covertType == 1 and file.endswith(".webp"):
            print("type 1 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "png")
        if covertType == 2 and file.endswith(".webp"):
            print("type 2 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "jpg")
        if covertType == 3 and file.endswith(".webp"):
            print("type 3 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "jpeg")
        if covertType == 4 and file.endswith(".jpg"):
            print("type 4 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "webp")
        if covertType == 5 and file.endswith(".jpeg"):
            print("type 5 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "webp")
        if covertType == 6 and file.endswith(".png"):
            print("type 6 -> covert file", file)
            im = Image.open(filePath).convert("RGB")
            im.save(filePath, "webp")


print("选择图片格式转换类型")
print("输入1 -> WebP to png")
print("输入2 -> WebP to jpg")
print("输入3 -> WebP to jpeg")
print("输入4 -> jpg to WebP")
print("输入5 -> jpeg to WebP")
print("输入6 -> png to WebP")

print("=======================")
print("请输入类型:")
type = input()
covertType = int(type)

if covertType < 1 or covertType > 6:
    print("输入了不支持的类型")
else:
    covertImage()

