
import os,sys
from core import dirOperate
import shutil
import core.loghelper as l


# 本脚本的用处：
#     调用文件夹操作类，获取需要复制的文件夹路径集合
#     根据目标路径，将文件夹集合复制到目标路径下

# targetPath=""
def batchMathchCopy(list,targetPath):
    #获取符合条件的文件夹路径集合
    list_sourceDir= dirOperate.getMatchDirList()
    # 复制文件夹至指定目录下
    for temp in list_sourceDir:
        shutil.copy(temp,targetPath)

def batchCopy(list,targetPath):
    log= l.logger('copyDirLog')
    # 复制文件夹至指定目录下
    for temp in list:
        srcname=temp.DirPath
        dstname=os.path.join(targetPath,temp.StationName,"GPS")
        try:
            if os.path.isdir(srcname):
                shutil.copytree(srcname,dstname)
                log.info("%s %s" % (temp, dstname))
            else:
                log.error("%s %s 已经存在指定目录" % (temp, dstname))
        # shutil.copy(temp.DirPath,os.path.join(targetPath,temp.StationName,"GPS"))
        except OSError as err:
            log.error("%s %s %s" % (temp, dstname,str(err)))
    log.info("——复制完成！——")
