
class StationInfo:
    def __init__(self,name,dir):
        self.StationName=name
        self.DirPath=dir

    def __str__(self):
        return ("name:%s|dir:%s"%(self.StationName,self.DirPath))