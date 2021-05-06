import os, shutil
import json
import threading
import random
import debug
import time
import common_var
import re
import common

import xml_sax

class AdbDyCtrl:
    """ adb操作接口 """
    def __init__(self, ident):
        self.dbg = debug.Debug()
        self.com = common.Common()
        self.gbl = common_var
        self.uixml = "ui_" + str(ident) + ".xml"                     #ui控件文件名称
        self.adbpath = self.gbl.path_adb                             #adb软件路径
        self.uixml_tmp = os.path.join(self.gbl.path_tmp, self.uixml) #ui控件全路径
        self.uixml_tmp2 = "/sdcard/" + self.uixml                    #终端里的 ui控件全路径
        self.dy_packet = "com.ss.android.ugc.aweme"                  #抖音包名称
        self.dy_activity = ".splash.SplashActivity"                  #抖音active名称(软件启动时使用)
    def sleeprandom(self, second):
        sec = int(second * 100)
        sec = random.randint(int(sec/10), sec)
        sec = sec / 100.0
        time.sleep(sec)
    def axisrandom(self, axis):
        """ 计算随机坐标 """
        ret = []
        try:
            x = random.randint(axis[0], axis[2]-1)
            y = random.randint(axis[1], axis[3]-1)
            ret.append(x)
            ret.append(y)
        except:
            self.dbg.printlog("err", ret)
        return ret
    def adb_run(self, adb_cmd):
        """ 运行adb命令, 有输出则返回输出, 没有则返回空字符串 """
        cmd = os.path.join(self.adbpath, adb_cmd)
        #self.dbg.printlog("trace", cmd)
        ret = ""
        with os.popen(cmd, 'r') as p:
            ret = p.read()
        #obj = os.popen(cmd)
        #if obj:
        #    ret = obj.read()
        #    obj.close()
        return ret
    def adb_ui_dump(self):
        """ 获取UI控件信息 """
        cmd = "adb shell uiautomator dump " + self.uixml_tmp2
        self.dbg.printlog("trace", cmd)
        ret = self.adb_run(cmd)
        if not ret:
            self.dbg.printlog("err", "Dump " + self.uixml + " false")
            return False
        #拷贝文件到win
        if os.path.exists(self.uixml_tmp):
            os.remove(self.uixml_tmp)
        cmd = "adb pull " + self.uixml_tmp2 + " " + self.uixml_tmp
        ret = self.adb_run(cmd)
        if not re.match(r"\[(100%)\]", ret):
            self.dbg.printlog("warnning", ret)
            #self.dbg.printlog("warnning", "Executing command: <" + cmd + "> false")
            #return False
        return True
    def adb_click(self, x, y):
        """ 点击 """
        cmd = "adb shell input tap " + str(x) + " " + str(y)
        #self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def click_random(self, axis):
        """ 给定坐标防范, 随机延时, 随机点击 """
        self.sleeprandom(0.5)
        axisrnd = self.axisrandom(axis)
        self.adb_click(axisrnd[0], axisrnd[1])
        self.sleeprandom(0.3)
    def adb_dy_start(self):
        """ 启动抖音软件 """
        cmd = "am start -n %s/%s" % (self.dy_packet, self.dy_activity)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_dy_stop(self):
        """ 关闭抖音软件 """
        cmd = "am force-stop %s" % (self.dy_packet)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_input(self, msg):
        """ 输入文件信息 """
        cmd = "adb shell input text %s" % (msg)
        self.dbg.printlog("trace", cmd)
        self.sleeprandom(0.4)
        self.adb_run(cmd)
        self.sleeprandom(0.5)
        pass
    def adb_slide(self, x1, y1, x2, y2):
        """ 滑动 """
        pass

class AdbDyThreadMain:
    """ 子线程主控制 """
    def __init__(self):
        self.gbl = common_var
        self.com = common.Common()
        self.status = self.gbl.SS_IDLE
        self.dbg = debug.Debug()
        self.adb = AdbDyCtrl("test")
        self.xaf = xml_sax.xml_attrs_finder()
        self.gaxis = self.gbl.get_axis("nova4")
        self.dbg.printlog("trace", self.gaxis)
        #环境信息
        evironment = {
            "status": self.gbl.SS_IDLE, #当前状态
            "page": self.gbl.PAGE_FCS,  #当前页
            "action": "initiong", #当前行为描述
            "vedio": "000", #当前操作的视频id
            "user": "000", #当前操作的用户
            "max": -1
        }
        #坐标信息
        self.vdoaxis = {
            "vdo_search_axis": [],  #焦点页视频搜索搜索关键字和坐标
            "vdo_first_axis" : [],   #第一个视频
            "vdo_main_axis" : [],    #主视频区坐标, 开始和暂停
            "vdo_stop_axis" : [],    #主视频区坐标, 开始和暂停
            "vdo_comment_axis" : [], #评论按钮
            "vdo_cmmt_user_axis" : [], #评论窗口用户头像坐标列表
            "vdo_cmmt_vdo_axis" : [], #评论页的视频页
            "vdo_user_axis" : [], #用户页抖音号
            "vdo_user_more_axis" : [], #用户页更多
            "vdo_user_cmmt_back_axis" : [], #用户页返回
            "vdo_user_info_back_axis" : [], #用户页返回
            "vdo_user_sendkey_axis" : [], #用户页发送私信按钮
            "vdo_user_sendcont_axis" : [], #用户页发送私信消息框
            "vdo_user_send_axis" : [], #用户页发送私信发送按钮
        }
    def axisrandom(self, axis):
        """ 计算随机坐标 """
        ret = []
        try:
            x = random.randint(axis[0], axis[2]-1)
            y = random.randint(axis[1], axis[3]-1)
            ret.append(x)
            ret.append(y)
        except:
            self.dbg.printlog("err", axis)
        return ret
    def axissync_get(self, page_key):
        axis = []
        if self.adb.adb_ui_dump():
            info = self.gbl.page_info[page_key]
            tag = info['tag']
            attrs = info['attrs']
            axis = self.xaf.get_axis(self.adb.uixml_tmp, tag, attrs)
        return axis
    def axissync(self, key):
        """ 成员坐标同步 """
        #坐标存在，直接返回
        if self.vdoaxis[key]:
            return self.vdoaxis[key]
        #从ui控件信息获取坐标值，并更新 self.vdoaxis
        if key == "vdo_search_axis":
            pass
        elif key == "vdo_first_axis":
            pass
        elif key == "vdo_main_axis":
            axis = []
            axis.append(self.gaxis[self.gbl.PAGE_FCS_VDO_RAW_WINDOW])
            self.vdoaxis[key] = axis
        elif key == "vdo_stop_axis":
            axis = []
            axis.append(self.gaxis[self.gbl.PAGE_FCS_VDO_RAW_WINDOW])
            self.vdoaxis[key] = axis
        elif key == "vdo_comment_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_CONTENT)
        elif key == "vdo_cmmt_user_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_LIST)
        elif key == "vdo_cmmt_vdo_axis":
            axis = []
            axis.append(self.gaxis[self.gbl.PAGE_FCS_VDO_CMMT_VDO_WINDOW])
            self.vdoaxis[key] = axis
        elif key == "vdo_user_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_ID)
        elif key == "vdo_user_more_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_MORE)
        elif key == "vdo_user_cmmt_back_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_BACK)
        elif key == "vdo_user_info_back_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_BACK)
        elif key == "vdo_user_sendkey_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_LTTR)
        elif key == "vdo_user_sendcont_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_LTTR_INPUT)
        elif key == "vdo_user_send_axis":
            self.vdoaxis[key] = self.axissync_get(self.gbl.PAGE_FCS_VDO_USER_LTTR_SEND)
        #返回成员变量，如果有获取到，则返回空表
        if not self.vdoaxis[key]:
            self.dbg.printlog("err", "Get axis false:", key)
        return self.vdoaxis[key]
    def ss_idle_proc(self):
        return self.gbl.SS_READY
    def ss_ready_proc(self):
        #搜索视频信息 PAGE_FCS
        #定位到第一个视频主页面 PAGE_FCS_VDO
        return self.gbl.SS_RUN
    def ss_run_proc(self):
        """ 私信轮询 """
        step = 1
        user_id_list = []
        user_axis_list = []
        user_axis_list_idx = 0
        while True:
            #S1 打开评论页
            if step == 1:
                #获取ui控件信息
                self.dbg.printlog("trace", "S1-1: get comment axis")
                axis_list = self.axissync("vdo_comment_axis")
                if not axis_list:
                    self.dbg.printlog("trace", "try get comment_axis again in S1")
                    axis = self.axissync("vdo_stop_axis")
                    self.dbg.printlog("tmp", "stop axis:", axis)
                    self.adb.click_random(axis[0])
                    step = 1
                    continue
                #点击评论
                self.dbg.printlog("trace", "S1-1: click comment axis")
                self.adb.click_random(axis_list[0])
                #判断用户信息
                if user_axis_list:
                    self.dbg.printlog("trace", "step = 3")
                    step = 3 #已经存在用户坐标信息，则跳过步骤2
                else:
                    self.dbg.printlog("trace", "step = 2")
                    step = 2
            #S2 获取UI控件信息的所有用户头像坐标
            if step == 2:
                self.dbg.printlog("trace", "S2: find all users")
                if self.adb.adb_ui_dump():
                    user_axis_list = self.axissync("vdo_cmmt_user_axis")
                    self.dbg.printlog("tmp", user_axis_list)
                if not user_axis_list:
                    #没有获取到用户评论页的ui控件情况，回到主视频页，点击暂停
                    axis = self.axissync("vdo_cmmt_vdo_axis")
                    self.adb.click_random(axis[0])
                    axis = self.axissync("vdo_stop_axis")
                    self.adb.click_random(axis[0])
                    self.dbg.printlog("trace", "step = 1")
                    step = 1
                    continue
                else:
                    self.dbg.printlog("trace", "step = 3")
                    step = 3
            #S3 遍历 user_axis_list
            if step == 3:
                self.dbg.printlog("trace", "S3: send message to all users")
                while user_axis_list_idx < len(user_axis_list):
                    axis = user_axis_list[user_axis_list_idx]
                    #点击用户头像
                    self.dbg.printlog("trace", "S3-1: click user head [", axis, "]")
                    self.adb.click_random(axis)
                    #获取抖音号
                    self.dbg.printlog("trace", "S3-2: get user id")
                    self.adb.adb_ui_dump()
                    info = self.gbl.page_info[self.gbl.PAGE_FCS_VDO_USER_ID]
                    tag = info['tag']
                    attrs = info['attrs']
                    keys = info['keys']
                    #self.dbg.printlog("tmp", "tag,attrs,keys =", tag, attrs, keys)
                    result = self.xaf.find_attrs(self.adb.uixml_tmp, tag, attrs, keys)
                    self.dbg.printlog("trace", "userid info:", result)
                    #判断抖音号是否已经操作过
                    userid = result[0][keys[0]]
                    if self.com.isin_list(user_id_list, userid):
                        self.dbg.printlog("trace", "user<" + userid + "> has been sent")
                    else:
                        user_id_list.append(userid)
                        #点击更多
                        self.dbg.printlog("trace", "S3-3: click user more")
                        axis = self.axissync("vdo_user_more_axis")
                        self.adb.click_random(axis[0])
                        #点击发送私信
                        self.dbg.printlog("trace", "S3-4: click send key")
                        axis = self.axissync("vdo_user_sendkey_axis")
                        self.adb.click_random(axis[0])
                        #点击发送消息框
                        self.dbg.printlog("trace", "S3-5: insert message in box")
                        axis = self.axissync("vdo_user_sendcont_axis")
                        self.adb.click_random(axis[0])
                        #输入消息内容
                        self.adb.adb_input("hello")
                        #点击发送
                        self.dbg.printlog("trace", "S3-6: send message")
                        #shutil.copy(self.adb.uixml_tmp, r"C:\ccx\workplace\python3\douyin_comments\tmp\ui9.xml")
                        axis = self.axissync("vdo_user_send_axis")
                        self.adb.click_random(axis[0])
                        #点击返回
                        self.dbg.printlog("trace", "S3-7: back from user")
                        axis = self.axissync("vdo_user_info_back_axis")
                        self.adb.click_random(axis[0])
                    #再次点击返回
                    self.dbg.printlog("trace", "S3-8: back from comment")
                    axis = self.axissync("vdo_user_cmmt_back_axis")
                    self.adb.click_random(axis[0])
                    #点击评论页的视频部分，进入完整视频页
                    self.dbg.printlog("trace", "S3-9: back to raw redio window")
                    axis = self.axissync("vdo_cmmt_vdo_axis")
                    self.dbg.printlog("trace", "cmmt out axis:", axis)
                    self.adb.click_random(axis[0])
                    #点击暂停
                    self.dbg.printlog("trace", "S3-10: pause vedio")
                    axis = self.axissync("vdo_stop_axis")
                    self.dbg.printlog("trace", "vdo stop axis:", axis)
                    self.adb.click_random(axis[0])
                    #点击评论按钮
                    self.dbg.printlog("trace", "S3-11: comment again")
                    axis = self.axissync("vdo_comment_axis")
                    self.adb.click_random(axis[0])
                    #用户数累计，同时记录相关信息
                    user_axis_list_idx = user_axis_list_idx + 1
                #一轮评论完毕
                step = 4
                user_axis_list_idx = 0
                user_axis_list = []
            #上滑，更新用户列表
            if step == 4:
                self.dbg.printlog("info", "user_id_list =", user_id_list)
                break
        self.adb.sleeprandom(3)
        return self.gbl.SS_RUN
    def ss_pause_proc(self):
        pass
    def ss_stop_proc(self):
        pass
    def ss_except_proc(self):
        pass
    def status_machine(self, msg):
        #定义状态字典
        status_dict = {
            SS_IDLE: ss_idle_proc,
            SS_READY: ss_ready_proc,
            SS_RUN: ss_run_proc,
            SS_PAUSE: ss_pause_proc,
            SS_STOP: ss_stop_proc
        }
        #运行状态函数
        proc = status_dict.get(self.status)
        if proc:
            self.status = proc(msg)
        else:
            self.status = self.ss_except_proc(msg)
    def main(self):
        msg = ""
        while True:
            self.status_machine(msg)
            
if (__name__ == "__main__"):
    """
    ident = "xx"
    adb = AdbDyCtrl(ident)
    ret = adb.sleeprandom(3)
    print(ret)
    """
    run = AdbDyThreadMain()
    run.ss_run_proc()
    


