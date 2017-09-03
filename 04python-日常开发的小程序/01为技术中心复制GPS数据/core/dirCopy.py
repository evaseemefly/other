
from core import dirOperate
import shutil


# 本脚本的用处：
#     调用文件夹操作类，获取需要复制的文件夹路径集合
#     根据目标路径，将文件夹集合复制到目标路径下

targetPath=""
def batchCopy(list):
    #获取符合条件的文件夹路径集合
    list_sourceDir= dirOperate.getMatchDirList()
    # 复制文件夹至指定目录下
    for temp in list_sourceDir:
        shutil.copy(temp,targetPath)
        