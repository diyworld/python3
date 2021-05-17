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
        sec = random.randint(int(sec/20), sec)
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
            self.dbg.printlog("err", axis)
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
        #self.dbg.printlog("tmp", cmd)
        self.adb_run(cmd)
    def click_random(self, axis):
        """ 给定坐标防范, 随机延时, 随机点击 """
        self.sleeprandom(0.5)
        axisrnd = self.axisrandom(axis)
        self.adb_click(axisrnd[0], axisrnd[1])
        self.sleeprandom(0.3)
    def adb_slide(self, x1, y1, x2, y2):
        """ 滑动 """
        cmd = "adb shell input swipe "\
            + str(x1) + " " + str(y1) + " "\
            + str(x2) + " " + str(y2)
        #self.dbg.printlog("tmp", cmd)
        self.adb_run(cmd)
    def slide_random(self, axis, length, dir):
        """ 给定坐标防范和滑动长度, 随机延时和滑动
            axis: 起点坐标范围
            length: 滑动长度
            dir: 方向, up/down/left/right
        """
        self.sleeprandom(0.5)
        axisrnd = self.axisrandom(axis)
        axisrnd2 = axisrnd.copy()
        if dir == 'up':
            axisrnd2[1] = (0) if (axisrnd2[1] < length) else (axisrnd2[1] - length)
            self.adb_slide(axisrnd[0], axisrnd[1], axisrnd2[0], axisrnd2[1])
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
        self.sleeprandom(0.3)
        self.adb_run(cmd)
        self.sleeprandom(0.3)
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
            "vdo_cmmt_content_axis" : [], #评论区坐标
            "vdo_cmmt_user_axis" : [], #评论窗口用户头像坐标列表
            "vdo_cmmt_vdo_axis" : [], #评论页的视频页
            "vdo_user_id" : [], #用户页抖音号
            "vdo_user_more_axis" : [], #用户页更多
            "vdo_user_cmmt_back_axis" : [], #用户评论页返回
            "vdo_user_info_back_axis" : [], #用户信息页返回
            "vdo_user_sendkey_axis" : [], #用户页发送私信按钮
            "vdo_user_sendcont_axis" : [], #用户页发送私信消息框
            "vdo_user_send_axis" : [], #用户页发送私信发送按钮
        }
    def attrs_get(self, page_idx, is_need_ui_dump):
        #获取ui控件里的指定属性信息
        #page_idx: 搜索的代号，每个代号在全局变量里都对应一个搜索参数
        #is_need_ui_dump: 是否需要重新获取ui控件信息
        #return: 返回列表，每个列表元素是一个字典，每个字典代表一行的健值对信息输出
        #根据page_idx，从全局变量里匹配到对应的 tag/attrs/keys
        #然后搜索.xml文件，搜索结果填充到返回值
        result = []
        if is_need_ui_dump:
            dump = self.adb.adb_ui_dump()
        if dump:
            info = self.gbl.page_info[page_idx]
            tag = info['tag']
            attrs = info['attrs']
            keys = info['keys']
            result = self.xaf.find_attrs(self.adb.uixml_tmp, tag, attrs, keys)
        return result
    def axissync_get(self, page_idx):
        axis = []
        if self.adb.adb_ui_dump():
            info = self.gbl.page_info[page_idx]
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
        elif key == "vdo_cmmt_content_axis":
            axis = []
            axis.append(self.gaxis[self.gbl.PAGE_FCS_VDO_CMMT_WINDOW])
            self.vdoaxis[key] = axis
        elif key == "vdo_cmmt_user_axis":
            #这里不仅仅要获取坐标值，还需要获取信息用于判断当前页面是否正常
            self.vdoaxis[key] = self.attrs_get(self.gbl.PAGE_FCS_VDO_USER_INFO)
            #把 bounds 元素放到列表的第一个元素位置
            for i, v in enumerate(self.vdoaxis[key]):
                if 'bounds' in v:
                    if i == 0:
                        break
                    else:
                        t = self.vdoaxis[key].pop(i)
                        self.vdoaxis[key].insert(0, t)
                        break
        elif key == "vdo_cmmt_vdo_axis":
            axis = []
            axis.append(self.gaxis[self.gbl.PAGE_FCS_VDO_CMMT_VDO_WINDOW])
            self.vdoaxis[key] = axis
        elif key == "vdo_user_id":
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
    def axis_ana(self, axis_str):
        """ 解析坐标 [x1,y1][x2,y2] -> [x1,y1,x2,y2] """
        taxis = []
        tt = re.match("\[([0-9]+),([0-9]+)\]\[([0-9]+),([0-9]+)\]", axis_str)
        if tt:
            taxis.append(int(tt.group(1)))
            taxis.append(int(tt.group(2)))
            taxis.append(int(tt.group(3)))
            taxis.append(int(tt.group(4)))
        return taxis
    def slideup(self): #上滑操作
        """ 评论页上滑操作 """
        self.adb.sleeprandom(1)
        axis = self.axissync("vdo_cmmt_content_axis")
        y1 = axis[1]
        y2 = axis[3]
        axis[1] = y2 - (y2 - y1) / 6
        length = (y2 - y1) * 4 / 6
        self.slide_random(axis, length, 'up')
    def check_page(self):
        #检查当前页面是否正常
        if not self.adb.adb_ui_dump():
            return False
        page = ""
        lst = []
        res = self.attrs_get(self.gbl.PAGE_FCS_VDO, True)
        lst.append(res)
        res = self.attrs_get(self.gbl.PAGE_FCS_VDO_CMMT, False)
        lst.append(res)
        res = self.attrs_get(self.gbl.PAGE_FCS_VDO_USER_ID, False)
        lst.append(res)
        res = self.attrs_get(self.gbl.PAGE_FCS_VDO_USER_LTTR, False)
        lst.append(res)
        self.dbg.printlog("trace", "lst =", lst)
        flg = [False, False, False, False]
        for v in (lst):
            for vv in v:
                if 'text' in vv:
                    if vv['text'].find("留下你的精彩评论吧") >= 0:
                        flg[0] = True #视频主页或评论页
                    if vv['text'].find("条评论") >= 0:
                        flg[1] = True #视频评论页
                    if vv['text'].find("抖音号") >= 0:
                        flg[2] = True #用户信息主页
                    if vv['text'].find("发私信") >= 0:
                        flg[3] = True #用户信息-更多
                    break
        if flg[0]:
            if flg[1]:
                #视频评论页
                page = self.gbl.PAGE_FCS_VDO
            else
                #视频主页
                page = self.gbl.PAGE_FCS_VDO_CMMT
        elif flg[2]:
            if flg[3]:
                #用户信息主页
                page = self.gbl.PAGE_FCS_VDO_USER_ID
            else
                #用户信息-更多
                page = self.gbl.PAGE_FCS_VDO_USER_LTTR
        else:
            self.dbg.printlog("err", "Not found any page")
        if page:
            return page
        return False
    def ss_run_proc(self):
        nextact = lambda a: nact if nact else a
        nact = ''
        st = 'S1'
        alst = [] #每个状态的当前行为指示器列表
        alst['S1'] = "get_comment_axis"
        user_id = ''
        user_id_list = [] #用户id列表
        cmmtui_info_list = [] #评论页ui信息列表
        err_count = 0 #临时错误计数器
        aaxis = [] #临时坐标
        last_cmmt_page = False #标识最后一页评论信息
        while True:
            self.dbg.pringlog("trace", ">>", st, alst[st])
            if st == 'S1': #主视频页
                if alst[st] == 'get_comment_axis':
                    #获取并点击坐标评论按钮
                    axis_list = self.axissync('vdo_comment_axis')
                    if not axis_list:
                        alst[st] = 'pause'
                        nact = 'get_comment_axit'
                        continue
                    self.adb.click_random(axis_list[0])
                    alst['S2'] = 'get_user_info_list'
                    st = 'S2'
                elif alst[st] == 'pause':
                    #暂停
                    axis_list = self.axissync("vdo_cmmt_vdo_axis")
                    self.adb.click_random(axis_list[0])
                    alst[st] = nextact('get_comment_axis')
                    nact = ''
                elif alst[st] == 'check':
                    page = self.check_page()
                    if not page:
                        err_count += 1
                        if err_count > 5:
                            err_count = 0
                            alst[st] = 'err_exit'
                            continue
                        alst[st] = 'pause'
                        nact = 'check'
                        continue
                    if page == self.gbl.PAGE_FCS_VDO:
                        #视频评论页
                        alst['S2'] = 'back'
                        st = 'S2'
                    elif page == self.gbl.PAGE_FCS_VDO_CMMT:
                        #视频主页
                        alst['S1'] = 'pause'
                    elif page == PAGE_FCS_VDO_USER_ID:
                        #用户信息主页
                        alst['S3'] = 'back'
                        st = 'S3'
                    elif page == PAGE_FCS_VDO_USER_LTTR:
                        #用户信息-更多
                        alst['S4'] = 'back'
                        st = 'S4'
                elif alst[st] == 'next_vedio':
                    #下一个视频，检查后才能上滑
                    page = self.check_page()
                    if page != self.gbl.PAGE_FCS_VDO:
                        alst[st] = 'pause'
                        nact = 'next_vedio'
                        continue
                    alst[st] = 'slide_up'
                elif alst[st] == 'slide_up':
                    #上滑操作
                    self.slideup()
                elif alst[st] == 'err_exit':
                    #异常退出
                    self.dbg.pringlog("err", "err_exit")
                    exit(0)
            elif st == 'S2': #视频评论页
                if alst[st] == "get_user_info_list":
                    #获取用户信息列表
                    if user_info_list:
                        #如果已经存在，则直接使用
                        alst[st] = "get_user_head"
                        continue
                    ui_info_list_idx = 0
                    ui_info_list = self.attrs_get(self.gbl.PAGE_FCS_VDO_USER_LIST, True)
                    t_info = self.attrs_get(self.gbl.PAGE_FCS_VDO_CONTENT_NOMORE, False)
                    self.dbg.printlog("trace", "ui_info_list =", ui_info_list)
                    self.dbg.printlog("trace", "t_info =", t_info)
                    if not ui_info_list:
                        #没有获取到，回退到视频页点击暂停后再来
                        alst['S1'] = 'pause'
                        alst[st] = 'back'
                        continue
                    if t_info and 'text' in t_info:
                        #最后一页评论信息
                        last_cmmt_page = True
                    alse[st] = 'get_user_head'
                elif alst[st] == 'get_user_head':
                    #逐个获取用户头像信息
                    ele = {}
                    if ui_info_list_idx >= len(ui_info_list):
                        #这次遍历结束
                        user_info_list = []
                        if last_cmmt_page:
                            #整个评论用户都以遍历结束
                            alst['S1'] = 'next_vedio'
                            alst[st] = back
                            continue
                        else:
                            #本页评论页的用户遍历结束
                            alst[st] = 'slide_up'
                            continue
                    ele = ui_info_list[ui_info_list_idx]
                    ui_info_list_idx += 1
                    if not ele or 'bounds' not in ele:
                        #如果不是头像坐标，则直接下一个
                        continue
                    if False:
                        #如果是第一个广告类型的头像，则直接下一个
                        #正常应该不会获取到这个信息
                        continue
                    #坐标转换为 [x1,y1,x2,y2]的形似，记录在 aaxis
                    aaxis = axis_ana(ele['bounds'])
                    alst[st] = 'click_user_head'
                elif alst[st] == 'click_user_head':
                    #点击用户头像
                    self.adb.click_random(aaxis)
                    alst['S3'] = 'get_user_ui_info'
                    st = 'S3'
                elif alst[st] == 'slide_up':
                    #评论信息上滑，获取新的评论
                    self.slideup()
                    alst[st] = 'get_user_info_list'
                elif alst[st] == 'back':
                    #回退
                    axis_list = self.axissync('vdo_user_cmmt_back_axis')
                    self.adb.click_random(axis_list[0])
                    alst['S1'] = 'pause'
                    st = 'S1'
            elif st == 'S3': #用户信息页
                if alst[st] == 'get_user_ui_info':
                    #获取用户ui控件信息
                    dyid = self.axissync('vdo_user_id')
                    if not dyid:
                        alst[st] = 'back'
                        alst['S2'] = 'back'
                        alst['S1'] = 'check'
                        continue
                    alst[st] = 'look_user_id'
                elif alst[st] == 'look_user_id':
                    #检查用户id信息
                    if user_id in user_id_list:
                        alst[st] = 'back'
                        alst['S2'] = 'get_user_head'
                        continue
                    alst[st] = 'click_user_more'
                elif alst[st] == 'click_user_more':
                    #点击更多
                    axis_list = self.axissync('vdo_user_more_axis')
                    self.adb.click_random(axis_list[0])
                    alst['S4'] = 'click_send_key'
                    st = 'S4'
                elif alst[st] == 'back':
                    #回退
                    axis_list = self.axissync('vdo_user_info_back_axis')
                    self.adb.click_random(axis_list[0])
                    st = 'S2'
            elif st == 'S4': #用户更多
                if alst[st] == 'click_send_key':
                    #点击发送私信按钮
                    pass
                elif alst[st] == 'back':
                    #回退
                    pass
            elif st == 'S5': #用户信息发送页
                elif alst[st] == 'click_send_box':
                    #点击发送私信信息框
                    pass
                elif alst[st] == 'input_msg':
                    #输入信息
                    pass
                elif alst[st] == 'send_msg':
                    #发送信息
                    pass
                elif alst[st] == 'back':
                    #回退
                    pass
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
    #run.slideup()
    run.ss_run_proc()
    


