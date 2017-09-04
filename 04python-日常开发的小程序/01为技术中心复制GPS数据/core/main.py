#!_*_coding:utf-8_*_
#from core import dirOperate
import dirOperate as do
import logger as lg

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
    sourcePath="E:\开发\01为单位开发的项目\other\04python-日常开发的小程序\01为技术中心复制GPS数据\test"
    menu_dic={
        "1":getExistGPSDirList
    }
    exit_flag=False
    while not exit_flag:
        print(menu_str)
        user_options=input("请输入对应编号").strip()
        if user_options in menu_dic:
            # 执行用户选择的菜单对应的方法
            menu_dic[user_options](sourcePath)
        else:
            print("\033[31;输入方法编号错误!\033[0m")



def getExistGPSDirList(sourcePath):
    '''
    根据指定的路径获取该路径下存在GPS子目录的所有文件夹名称，并导出
    :param sourcePath:
    :return:
    '''
    # 获取符合条件的集合
    list_dir=do.getMatchDirList()
    logger= lg.logger('existDirLog')
    # 写入日志文件中
    for temp in list_dir:
        logger.info(temp)


def run():
    interactive()

if __name__=="__main__":
    run()
