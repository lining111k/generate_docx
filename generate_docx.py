import shutil
import os
# 定义人名列表
names = ["李宁_202221140149", "陈嘉贤_202221140148", "邹鹏钰_202221140150", "马睿-202252140230",
         "刘颖-202122140225","邱晨曦-202321140152"]

# 指定原始DOCX文件路径
original_docx_path = "原版文件.docx"
mouth = 10
os_name = f"第{mouth}月心理晴雨表"
# 创建一个文件夹来保存生成的文件
if not os.path.exists(os_name):
    os.makedirs(os_name)
mouth = 10
# 遍历人名列表，为每个名字生成一个新文件
for name in names:
    # 根据名字生成新文件名
    output_file_name = f"{os_name}/{name}-第{mouth}月心理晴雨表.docx"

    # 复制原始DOCX文件到新文件
    shutil.copy(original_docx_path, output_file_name)

print("Files generated successfully!")
