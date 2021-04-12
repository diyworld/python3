import os
import threading

# 公共索引
class GVar:
    """ 资源锁 """
    lock = threading.Lock()
    """ 定义页面标识, 只读 """
    PAGE_MAIN = 1   #主页面
    #视频页
    #最上一栏为[地点名称 关注 @推荐], 最下方一栏为[@首页 朋友 + 消息 我]
    PAGE_VDO = 2
    PAGE_VDO_CMMT = 21  #视频评论页面
    PAGE_VDO_USER = 22   #用户页面
    PAGE_VDO_USER_MORE = 221 #用户更多页面
    PAGE_VDO_USER_LTTR = 222 #用户私信页面
    PAGE_VDO_USER_WRITE = 223 #用户私信发送页面
    #视频焦点页
    #点击搜索后, 选择视频[综合 @视频 用户 商品 直播 ...]
    PAGE_FCS = 3
    PAGE_FCS_VDO = 30 #视频
    PAGE_FCS_VDO_CMMT = 31  #视频评论页面
    PAGE_FCS_VDO_USER = 32   #用户页面
    PAGE_FCS_VDO_USER_MORE = 321 #用户更多页面
    PAGE_FCS_VDO_USER_LTTR = 322 #用户私信页面
    PAGE_FCS_VDO_USER_WRITE = 323 #用户私信发送页面
    
    """ 目录路径, 读写 """
    #数据记录目录
    path_record = r"C:\ccx\workplace\python3\douyin_comments\record"
    #ADB软件目录
    path_adb = r"C:\ccx\workplace\ADB\Minimal ADB and Fastboot"
    #临时目录
    path_tmp = r"C:\ccx\workplace\python3\douyin_comments\tmp"
    
    """ ADB命令 """
    
    
    """ 全局方法接口 """
    def __init__(self):
        pass
    def set_path_record(self, path):
        GVar.lock.acquire()
        self.path_record = path
        GVar.lock.release()
    def set_path_adb(self, path)
        GVar.lock.acquire()
        self.path_adb = path
        GVar.lock.release()
    def set_path_tmp(self, path)
        GVar.lock.acquire()
        self.path_tmp = path
        GVar.lock.release()

