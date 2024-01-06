import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
import io

# 设置标准输出流的编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def show_help_message():
    help_message = (
        "欢迎使用MSFS2020 Map Enhancement 汉化软件 \n"
        "在安装汉化前，请确保已经安装好了原版软件，并知道软件的安装路径， \n"
        "检查软件是否已经关闭， \n"
        "请在弹出的对话框中选择包含 'resources' 文件夹的目标文件夹， \n"
        "例如：'C:\Program Files\MSFS2020 Map Enhancement' \n"
        "保证选择的目录下有'resources'文件夹！\n"
        "汉化作者：YangXiaoMian"
    )
    messagebox.showinfo("帮助信息", help_message)

def replace_asar_folder():
    # 提示用户选择文件夹
    show_help_message()

    # 获取用户选择的文件夹路径
    folder_path = filedialog.askdirectory(title="选择文件夹")
    
    if folder_path:
        # 拼接资源文件夹路径和目标文件路径
        resources_folder = os.path.join(folder_path, 'resources')
        target_asar_path = os.path.join(resources_folder, 'app.asar')
        source_asar_path = os.path.join(os.getcwd(), 'file', 'app.asar')

        # 检查目标文件是否存在，存在则替换
        if os.path.exists(target_asar_path):
            shutil.copyfile(source_asar_path, target_asar_path)
            print("替换成功！")
            
            # 添加消息框提示替换成功
            messagebox.showinfo("替换成功", "替换成功！")
            sys.exit()  # 退出整个程序

        else:
            print("目标文件不存在，请检查文件夹路径是否正确.")

# 创建简单的GUI窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 执行替换操作
replace_asar_folder()

# 保持主窗口运行，直到用户手动关闭
root.mainloop()
