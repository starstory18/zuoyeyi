import re
import csv
import os
import shutil
from urllib import request

# 定义正则表达式匹配模式
department_pattern = r'<span class="iden">(.*?)</span>'
name_pattern = r'<span class="name">(.*?)</span>'
photo_pattern = r'<img src="(.*?)"'
#<img src="/__local/8/C7/01/CEA77732C1F6EA3AA3A47F69E21_33E46CCF_44BE2.jpg" alt="">
#r'<img src="(.*?)"'
# 读取HTML文件并解析

with open('./副教授-数字媒体与设计艺术学院.html', 'r', encoding='utf-8') as file:
    html = file.read()

    # 匹配教师信息
    departments = re.findall(department_pattern, html)
    teachers = re.findall(name_pattern, html)
    photos = re.findall(photo_pattern, html)
    photos.pop(0) #切除前两个多余元素
    photos.pop(0)

# 将解析结果保存到CSV文件中
with open('teachers.csv', 'a+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Depatment','Name','Title','Photo'])

    for i in range(len(teachers)):
        department = departments[i]
        name = teachers[i]
        photo_url = photos[i]
        writer.writerow([department,name, '副教授', photo_url])

with open('./教授-数字媒体与设计艺术学院.htm', 'r', encoding='utf-8') as file:
    html = file.read()

    # 匹配教师信息
    departments = re.findall(department_pattern, html)
    teachers = re.findall(name_pattern, html)
    photos = re.findall(photo_pattern, html)
    photos.pop(0) #切除前两个多余元素
    photos.pop(0)

# 将解析结果保存到CSV文件中
with open('teachers.csv', 'a+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    for i in range(len(teachers)):
        department = departments[i]
        name = teachers[i]
        photo_url = photos[i]
        writer.writerow([department,name, '教授', photo_url])

with open('./讲师-数字媒体与设计艺术学院.htm', 'r', encoding='utf-8') as file:
    html = file.read()

    # 匹配教师信息
    departments = re.findall(department_pattern, html)
    teachers = re.findall(name_pattern, html)
    photos = re.findall(photo_pattern, html)
    photos.pop(0) #切除前两个多余元素
    photos.pop(0)

# 将解析结果保存到CSV文件中
with open('teachers.csv', 'a+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    for i in range(len(teachers)):
        department = departments[i]
        name = teachers[i]
        photo_url = photos[i]
        writer.writerow([department,name, '讲师', photo_url])




#头像下载
source_folder1 = './副教授-数字媒体与设计艺术学院_files'
source_folder2 = './教授-数字媒体与设计艺术学院_files'
source_folder3 = './讲师-数字媒体与设计艺术学院_files'
# 源文件夹路径
destination_folder = 'tupian'  # 目标文件夹路径

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder1):
    if filename.endswith('.jpg'):
        source_file_path = os.path.join(source_folder1, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        shutil.copy(source_file_path, destination_file_path)

for filename in os.listdir(source_folder2):
    if filename.endswith('.jpg'):
        source_file_path = os.path.join(source_folder2, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        shutil.copy(source_file_path, destination_file_path)

for filename in os.listdir(source_folder3):
    if filename.endswith('.jpg'):
        source_file_path = os.path.join(source_folder3, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        shutil.copy(source_file_path, destination_file_path)

print("图片下载完成！")

print("信息爬取成功！")

