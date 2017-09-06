#!_*_coding:utf-8_*_
#from core import dirOperate
# import
import core.dirOperate as do
import core.dirCopy as dc
import core.loghelper as lg
import conf.settings as st
import model.model as md
# from conf import settings as st





def interactive():
    '''
    交互方法
    :param data:
    :return:
    '''
    menu_str=u'''
    ——————菜单——————
      \033[32;1m1.  导出当前存在GPS路径的文件夹列表
    2. 复制当前路径下的全部GPS文件    
    6.  退出
    \033[0m
    '''
    sourcePath = st.SOURCE_DIR
    targetPath=st.TARGET_DIR
    stations=st.STATIONS
    menu_dic={
        "1":getExistGPSDirList,
        "2":copySource2TargetPath
    }
    exit_flag=False
    while not exit_flag:
        print(menu_str)
        user_options=input("请输入对应编号").strip()
        d1={'targetPath':targetPath,
            'stations':stations}
        if user_options in menu_dic:
            # 执行用户选择的菜单对应的方法
            menu_dic[user_options](sourcePath,**d1)
        else:
            print("\033[31;输入方法编号错误!\033[0m")



def getExistGPSDirList(sourcePath,islog=1,**kwargs):
    '''
    根据指定的路径获取该路径下存在GPS子目录的所有文件夹名称，并导出
    :param sourcePath:
    :return:将存在的目录返回
    '''
    # 获取符合条件的集合
    source=sourcePath
    list_fulldirName,list_dir=getMathchDir(sourcePath)
    if islog:
        loghelper= lg.logger('existDirLog')
        # 写入日志文件中
        for temp in list_fulldirName:
            loghelper.info(temp)
    return list_fulldirName,list_dir

def getMathchDir(sourcePath):
    source = sourcePath
    list_fulldirName, list_dir = do.getMatchDirList(source)
    return list_fulldirName,list_dir

def copySource2TargetPath(sourcePath,**kwargs):
    '''
    1、根据传入的目录sourcePath获取该路径下的海洋站列表
    2、list_dir与stations进行匹配，取交集
    3、复制剩余的目录至targetPath
    :return:
    '''

    # 1
    list_fulldirName,list_dir= getMathchDir(sourcePath)
    targetPath=kwargs['targetPath']
    # 获取海洋站数组
    stations= kwargs['stations']
    index=0
    list_stationInfo=[]
    # 对list_fulldirName进行处理，获得最终的需要复制的list_fulldirName
    # 循环当前存在的station列表[]
    for dir in list_dir:
        # 判断当前的temp是否在需要复制的海洋站列表[]中
        if dir in stations:
            list_stationInfo.append(md.StationInfo(dir,list_fulldirName[index]))
        # if dir not in stations:
        #     # 若当前temp不在需要复制的列表中，则将该temp对应下标的存储路径数组中剔除该下标的对象
        #     list_fulldirName.pop(index)
        index+=1
    # 2 批量复制
    # 对对list_fulldirName批量复制到targetPath下

    dc.batchCopy(list_stationInfo,targetPath)


# def getMathStations(list_dir,stations):
#     '''
#
#     :param list_dir: 文件夹集合
#     :param stations:海洋站数组
#     :return:
#     '''
#     for dir in list_dir:
#         if

def run():
    interactive()

