import os
import threading

import time
import debug
import common

class source:
    # 共享资源
    # !!! 在 source 中使用 source.xxx
    lock = threading.Lock()
    video_list = []#[{video_id, status, [user_id]}]
    user_list = [] #[{user_id, status, [video_id]}]
    def video_clear(self):
        source.lock.acquire()
        source.video_list = []
        source.lock.release()
    def user_clear(self):
        source.lock.acquire()
        source.user_list = []
        source.lock.release()
    def video_write(self, fullpath):
        """ 视频信息写入文件 """
        ret = True
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        source.lock.acquire()
        #fullpath = os.path.join(source.record_path, source.videofile_name)
        try:
            fd = open(fullpath, "a")
            fd.write(str("\n---- " + curtime + " ----\n"))
            fd.write(str(source.video_list))
            fd.close()
        except:
            print("[write_video_file] open and write failed")
            ret = False
        source.lock.release()
        return ret
    def user_write(self, fullpath):
        """ 用户信息写入文件 """
        ret = True
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        source.lock.acquire()
        #fullpath = os.path.join(source.record_path, source.userfile_name)
        try:
            fd = open(fullpath, "a")
            fd.write(str("\n---- " + curtime + " ----\n"))
            fd.write(str(source.user_list))
            fd.close()
        except:
            print("[write_user_file] open and write failed")
            ret = False
        source.lock.release()
        return ret
    def video_get(self, video_id):
        """ 查找视频元素 """
        ret = {}
        source.lock.acquire()
        for ele in source.video_list:
            if ele['video_id'] == video_id:
                ret = ele
                break
        source.lock.release()
        return ret
    def video_insert(self, element):
        """ 插入视频元素 """
        source.lock.acquire()
        source.video_list.append(element)
        source.lock.release()
        return True
    def video_adduser(self, video_id, user_id):
        """ 在视频节点域插入用户id """
        ele = {}
        source.lock.acquire()
        for ele in source.video_list:
            if ele['video_id'] == video_id:
                ret = ele
                break
        try:
            ele['user_id_list'].append(user_id)
        except:
            print("[video_adduser] append failed")
        source.lock.release()
    def user_get(self, user_id):
        """ 查找用户记录 """
        ret = {}
        source.lock.acquire()
        for ele in source.user_list:
            if ele['user_id'] == user_id:
                ret = ele
                break
        source.lock.release()
        return ret
    def user_insert(self, element):
        """ 插入用户元素 """
        source.lock.acquire()
        source.user_list.append(element)
        source.lock.release()
        return True
    def user_addvideo(self, user_id, video_id):
        """ 在用户节点域插入视频id """
        ele = {}
        source.lock.acquire()
        for ele in source.user_list:
            if ele['user_id'] == user_id:
                ret = ele
                break
        try:
            ele['video_id_list'].append(video_id)
        except:
            print("[user_addvideo] append failed")
        source.lock.release()
        return True
    def show(self):
        source.lock.acquire()
        print("video_list =", source.video_list)
        print("user_list =", source.user_list)
        source.lock.release()
        return True

class dy_log:
    """ dy日志操作 
        !!! 在类 dy_log 中使用 source().xxx
        !!! 在类 source 中使用 source.xxx
    """
    def __init__(self):
        self.record_path = ""
        self.userfile = "user_info.txt"
        self.videofile = "video_info.txt"
        self.wflag = False
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
            source().video_write(video_fullpath)
            source().user_write(user_fullpath)
            source().video_clear()
            source().user_clear()
        except:
            is_sync_ok = False
            print("[sync_to_file] sync failed")
        return is_sync_ok
    def is_user_exist(self, user_id):
        """ 判断用户是否有记录 """
        ele = source().user_get(user_id)
        return True if ele else False
    def is_video_exist(self, video_id):
        """ 判断视频是否有记录 """
        ele = source().video_get(video_id)
        return True if ele else False
    def isin_user_of_video(video_id, user_id):
        """ 判断视频列表里是否已经有该用户的记录 """
        ele = source().video_get(video_id)
        if user_id in ele['user_id_list']:
            return True
        return False
    def isin_video_of_user(user_id, video_id):
        """ 判断用户列表里是否已经有该视频记录 """
        ele = source().user_get(user_id)
        if video_id in ele['video_id_list']:
            return True
        return False
    def insert(self, video_id, video_st, user_id, user_st):
        """ 给定一组视频号, 用户号, 和对应状态, 自动将数据插入到对应列表 """
        ele = {}
        ###
        video_ele = source().video_get(video_id)
        if not video_ele:
            # 创建视频元素
            ele = {
                "video_id": video_id,
                "status": video_st,
                "user_id_list": [user_id]
            }
            source().video_insert(ele)
        else:
            # 直接插入
            source().video_adduser(video_id, user_id)
        # 创建用户元素
        user_ele = source().user_get(user_id)
        if not user_ele:
            ele = {
                "user_id": user_id,
                "status": user_st,
                "video_id_list": [video_id]
            }
            source().user_insert(ele)
        else:
            # 直接插入
            source().user_addvideo(user_id, video_id)
        return True
    def show(self):
        source().show()
        return True
    

