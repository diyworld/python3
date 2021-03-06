import os, re
import threading

import time
import debug
import common

class Source:
    # 共享资源
    lock = threading.Lock()
    video_list = []#[{video_id, status, [user_id]}]
    user_list = [] #[{user_id, status, [video_id]}]
    def video_clear(self):
        Source.lock.acquire()
        Source.video_list = []
        Source.lock.release()
    def user_clear(self):
        Source.lock.acquire()
        Source.user_list = []
        Source.lock.release()
    def video_write(self, fullpath):
        """ 视频信息写入文件 """
        ret = True
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Source.lock.acquire()
        #fullpath = os.path.join(Source.record_path, Source.videofile_name)
        try:
            fd = open(fullpath, "a")
            fd.write(str("\n---- " + curtime + " ----\n"))
            fd.write(str(Source.video_list))
            fd.close()
        except:
            print("[write_video_file] open and write failed")
            ret = False
        Source.lock.release()
        return ret
    def user_write(self, fullpath):
        """ 用户信息写入文件 """
        ret = True
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Source.lock.acquire()
        #fullpath = os.path.join(Source.record_path, Source.userfile_name)
        try:
            fd = open(fullpath, "a")
            fd.write(str("\n---- " + curtime + " ----\n"))
            fd.write(str(Source.user_list))
            fd.close()
        except:
            print("[write_user_file] open and write failed")
            ret = False
        Source.lock.release()
        return ret
    def video_get(self, video_id):
        """ 查找视频元素 """
        ret = {}
        Source.lock.acquire()
        for ele in Source.video_list:
            if ele['video_id'] == video_id:
                ret = ele
                break
        Source.lock.release()
        return ret
    def video_insert(self, element):
        """ 插入视频元素 """
        Source.lock.acquire()
        Source.video_list.append(element)
        Source.lock.release()
        return True
    def video_adduser(self, video_id, user_id):
        """ 在视频节点域插入用户id """
        ele = {}
        Source.lock.acquire()
        for ele in Source.video_list:
            if ele['video_id'] == video_id:
                ret = ele
                break
        try:
            ele['user_id_list'].append(user_id)
        except:
            print("[video_adduser] append failed")
        Source.lock.release()
    def user_get(self, user_id):
        """ 查找用户记录 """
        ret = {}
        Source.lock.acquire()
        for ele in Source.user_list:
            if ele['user_id'] == user_id:
                ret = ele
                break
        Source.lock.release()
        return ret
    def user_insert(self, element):
        """ 插入用户元素 """
        Source.lock.acquire()
        Source.user_list.append(element)
        Source.lock.release()
        return True
    def user_addvideo(self, user_id, video_id):
        """ 在用户节点域插入视频id """
        ele = {}
        Source.lock.acquire()
        for ele in Source.user_list:
            if ele['user_id'] == user_id:
                ret = ele
                break
        try:
            ele['video_id_list'].append(video_id)
        except:
            print("[user_addvideo] append failed")
        Source.lock.release()
        return True
    def show(self):
        Source.lock.acquire()
        print("video_list =", Source.video_list)
        print("user_list =", Source.user_list)
        Source.lock.release()
        return True

class Dy_log:
    """ Dy日志操作 
        !!! 在类中调用方法必须是实例调用 Source().xxx !!!
    """
    def __init__(self):
        self.record_path = ""
        self.userfile = "user_info.txt"
        self.videofile = "video_info.txt"
        self.wflag = False
        self.source = Source()
    def setpath(self, path):
        """ 设置存储路径 """
        if len(path) == 0:
            print("path is null")
            return False
        elif not os.path.exists(path):
            print("[setpath] path doesn't exist")
            return False
        elif os.path.isfile(path):
            print("param isn't a path but file")
            return False
        self.record_path = path
        self.wflag = True
        return True
    def clrpath(self):
        """ 清除日志存储路径 """
        self.wflag = False
        self.record_path = ""
        return True
    def sync_to_file(self):
        """ 同步变量数据到文件, 成功后清除变量内容 """
        is_sync_ok = True
        video_fullpath = os.path.join(self.record_path, self.videofile)
        user_fullpath = os.path.join(self.record_path, self.userfile)
        try:
            self.source.video_write(video_fullpath)
            self.source.user_write(user_fullpath)
            self.source.video_clear()
            self.source.user_clear()
        except:
            is_sync_ok = False
            print("[sync_to_file] sync failed")
        return is_sync_ok
    def is_user_exist(self, user_id):
        """ 判断用户是否有记录 """
        ele = self.source.user_get(user_id)
        return True if ele else False
    def is_video_exist(self, video_id):
        """ 判断视频是否有记录 """
        ele = self.source.video_get(video_id)
        return True if ele else False
    def isin_user_of_video(video_id, user_id):
        """ 判断视频列表里是否已经有该用户的记录 """
        ele = self.source.video_get(video_id)
        if user_id in ele['user_id_list']:
            return True
        return False
    def isin_video_of_user(user_id, video_id):
        """ 判断用户列表里是否已经有该视频记录 """
        ele = self.source.user_get(user_id)
        if video_id in ele['video_id_list']:
            return True
        return False
    def insert(self, video_id, video_st, user_id, user_st):
        """ 给定一组视频号, 用户号, 和对应状态, 自动将数据插入到对应列表 """
        ele = {}
        ###
        video_ele = self.source.video_get(video_id)
        if not video_ele:
            # 创建视频元素
            ele = {
                "video_id": video_id,
                "status": video_st,
                "user_id_list": [user_id]
            }
            self.source.video_insert(ele)
        else:
            # 直接插入
            self.source.video_adduser(video_id, user_id)
        # 创建用户元素
        user_ele = self.source.user_get(user_id)
        if not user_ele:
            ele = {
                "user_id": user_id,
                "status": user_st,
                "video_id_list": [video_id]
            }
            self.source.user_insert(ele)
        else:
            # 直接插入
            self.source.user_addvideo(user_id, video_id)
        return True
    def show(self):
        self.source.show()
        return True
    
class class_store_log:
    """
    视频号和用户号，获取一次存储一次
    文件名取为搜索关键字
    开始时读取并载入该文件
    一个线程维护一个log对象，一个log对象维护一个文件
    """
    def __init__(self, fullpath):
        self.dbg = debug.Debug()
        self.comm = common.Common()
        self.recordfile = fullpath
        self.user_id_list = []
        self.user_id_list_commit_idx = 0
        self.setpath(fullpath)
    def setpath(self, fullpath):
        """ 设置存储文件 """
        if len(fullpath) == 0:
            self.dbg.printlog("trace", "fullpath is null")
            return False
        elif not os.path.exists(fullpath):
            #文件不存在，则创建
            self.dbg.printlog("trace", "create fullpath")
            curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            try:
                fd = open(fullpath, "a")
                fd.write(str("---- " + curtime + " ----\n"))
                self.recordfile = fullpath
                fd.close()
            except:
                self.dbg.printlog("err", "open and write failed")
                return False
        else:
            #如果文件存在，则载入文件内容
            lst = self.comm.readfile(self.recordfile, 'line')
            for i in range(len(lst)):
                if lst[i].find('----') == -1:
                    self.user_id_list.append(lst[i])
            self.user_id_list_commit_idx = len(self.user_id_list)
            #self.dbg.printlog("trace", "user_id_list =", self.user_id_list)
        return True
    def user_insert(self, user_id):
        #插入 user_id 到列表
        if user_id:
            self.user_id_list.append(user_id)
    def is_user_exist(self, user_id):
        #判断用户是否已经存在
        #self.dbg.printlog("tmp", "user_id =", user_id)
        #self.dbg.printlog("tmp", "user_id_list =", self.user_id_list)
        if user_id in self.user_id_list:
            return True
        return False
    def commit(self):
        #同步 user_id_list 列表到文件
        try:
            list_len = len(self.user_id_list)
            if list_len > 0:
                fd = open(self.recordfile, "a")
                curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                fd.write(str("---- " + curtime + " ----\n"))
                for i in range(self.user_id_list_commit_idx, list_len):
                    #self.dbg.printlog("trace", "add user id: ", self.user_id_list[i])
                    fd.write(self.user_id_list[i] + '\n')
                fd.close()
            self.user_id_list_commit_idx = list_len
            self.dbg.printlog("trace", "commit success")
        except:
            self.dbg.printlog("err", "commit failed")
            return False
        return True




