
import os
import re #正则表达式库
# 原始路径
sourcePath=""
#目标路径
targetPath=""

#获取原始路径下符合条件的路径
def getMatchDirList(self):
    # 1 获得原始路径下的全部文件夹集合
    list_sourcepaht_dir= os.listdir(sourcePath)
    # 2 筛选list，使用正则表达式匹配中文开头的文件夹
    # 获取符合条件的文件夹集合
    list_dirmatch=filter(isStationNameRex,list_sourcepaht_dir)

    list_fulldirfinal=[]
    # 3 获取最终的文件夹集合
    # 判断该文件夹下是否存在GPS子文件夹
    os.path.join(sourcePath,)
    for dir in list_dirmatch:
        sourceFullDir_temp=os.path.join(sourcePath,"dir","GPS")
        # 若原始文件夹中存在GPS子文件夹则记录在新创建的list中
        if isExistGPSDir(sourceFullDir_temp):
            list_fulldirfinal.append(sourceFullDir_temp)
    return list_fulldirfinal

def isExistGPSDir(obj):
    return os.path.exists(obj)

def isStationNameRex(obj):
    # 匹配所有中文开头，期间有n个中文字符，后面也可以有英文的规则
    return matchRex(obj,r'^[\u4E00-\u9FA5]+*$')

def matchRex(obj,re):
    return re.match(re,obj)

