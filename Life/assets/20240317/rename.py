# import os

# # 文件夹路径
# folder_path = 'docs/Life/assets/20240317'

# # 获取文件夹内的所有文件列表
# files = os.listdir(folder_path)

# i = 15
# # 重命名文件
# for index, file in enumerate(files, start=1):
#     if(file[-3:] == 'jpg'):
#         # 构建新的文件名
#         new_file_name = f"pic_{i:03d}.jpg"  # 例如：001_file.txt
        
#         # 获取原文件的完整路径
#         old_file_path = os.path.join(folder_path, file)
        
#         # 获取新文件的完整路径
#         new_file_path = os.path.join(folder_path, new_file_name)
        
#         # 重命名文件
#         os.rename(old_file_path, new_file_path)

#         i = i + 1

# print("文件重命名完成。")

s = '![](./assets/20240317/pic'


for i in range(23) :
    a = f"{s}_{i:03d}.jpg)"

    print(a)
