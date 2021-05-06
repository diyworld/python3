import os
import re
import threading

"""@*******************************************************************
    配置信息
*******************************************************************@"""
#ADB软件目录
path_adb = r"C:\ccx\workplace\ADB\Minimal_ADB_and_Fastboot"
#临时目录
path_tmp = r"C:\ccx\workplace\python3\douyin_comments\tmp"
#日志文件存放路径
log_path = r"C:\ccx\workplace\python3\douyin_comments\record"
#视频类目
vedio_type = [
    {
        'key': "中国最美公路", #关键词
        'terminal_count': 1,   #终端数
        'trave_mode': "LR", #评论遍历模式
        'user_max': -1      #用户上限数
    },{
        'key': "中国最美姑娘", #关键词
        'terminal_count': 1,   #终端数
        'trave_mode': "LR", #评论遍历模式
        'user_max': -1      #用户上限数
    }
]
#终端信息
termianl_info = [
    {
        'name': "nova4",
        'ratio': "900*1600"
    },{
        'name': "iphone5",
        'ratio': "900*1600"
    }
]

"""@*******************************************************************
    公共索引
*******************************************************************@"""
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
PAGE_FCS_SEARCH = 301
PAGE_FCS_INPUT = 302
PAGE_FCS_INPUT_OK = 303
PAGE_FCS_VEDIO = 304
PAGE_FCS_VEDIO_FIRST = 305
#视频页
PAGE_FCS_VDO = 30 #视频
PAGE_FCS_VDO_CONTENT = 3001
PAGE_FCS_VDO_CONTENT_NOMORE = 3002
PAGE_FCS_VDO_PLAY_STOP = 3003
PAGE_FCS_VDO_RAW_WINDOW = 3004 #视频页主窗口
#评论页
PAGE_FCS_VDO_CMMT = 31  #视频评论页面
PAGE_FCS_VDO_CMMT_BACK = 3101
PAGE_FCS_VDO_CMMT_COUNT = 3102 #168条评论
PAGE_FCS_VDO_CMMT_WINDOW = 3103 #评论主窗口
PAGE_FCS_VDO_CMMT_VDO_WINDOW = 3104 #带评论时的视频窗口
PAGE_FCS_VDO_CMMT_INPUT = 3105
#用户页面
PAGE_FCS_VDO_USER = 32
PAGE_FCS_VDO_USER_LIST = 3201
PAGE_FCS_VDO_USER_MORE = 3202
PAGE_FCS_VDO_USER_BACK = 3203
PAGE_FCS_VDO_USER_ID = 3204
#用户私信页面
PAGE_FCS_VDO_USER_LTTR = 322
PAGE_FCS_VDO_USER_LTTR_INPUT = 32201
PAGE_FCS_VDO_USER_LTTR_BACK = 32202
#用户私信发送页面
PAGE_FCS_VDO_USER_WRITE = 323
PAGE_FCS_VDO_USER_LTTR_SEND = 32301

#异常页
PAGEERR_UPDATE = 4
PAGEERR_UPDATE_FLAG = 401
PAGEERR_UPDATE_CANCEL = 402

"""@*******************************************************************
    状态定义
*******************************************************************@"""
#主线程状态定义
SM_IDLE = 1    #空闲状态
SM_READY = 2   #数据检查，准备阶段
SM_SYNC = 3    #数据同步
SM_RUN = 4     #运行
SM_PAUSE = 5   #暂停
SM_STOP = 6    #停止
SM_ERROR = 7   #错误状态
#子线程状态定义
SS_IDLE = 1    #线程启动后初始化完成，等待进一步指令
SS_READY = 2   #收到启动指令后检查线程和操作环境
SS_RUN = 3     #运行
SS_PAUSE = 4   #暂停
SS_STOP = 5    #停止
SS_ERROR = 7   #错误状态

#xml 坐标定位信息索引表
page_info = {
    # 视频焦点页
    #视频搜索
    ##搜索
    PAGE_FCS_SEARCH:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/dzo"},"keys":["bounds"]},
    ##输入
    PAGE_FCS_INPUT:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/aop"},"keys":["bounds"]},
    ##输入确定
    PAGE_FCS_INPUT_OK:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/kla"},"keys":["bounds"]},
    ##定位视频标签
    PAGE_FCS_VEDIO:{"tag":"node","attrs":{"resource-id":"android:id/text1"},"keys":["bounds"]},
    ##选择第一个视频
    PAGE_FCS_VEDIO_FIRST:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/f7s"},"keys":["bounds"]},
    ##视频评论
    PAGE_FCS_VDO_CONTENT:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/b98"},"keys":["bounds"]},
    ##用户遍历, 通过 xxx的头像 找到对应坐标列表
    PAGE_FCS_VDO_USER_LIST:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/jv"},"keys":["bounds"]},
    ##用户遍历标志: 暂时没有更多了
    PAGE_FCS_VDO_CONTENT_NOMORE:{"tag":"node","attrs":{"text":"暂时没有更多了","class":"android.widget.TextView"},"keys":["bounds"]},
    #用户页面
    ##更多
    PAGE_FCS_VDO_USER_MORE:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/jfv"},"keys":["bounds"]},
    ##返回
    PAGE_FCS_VDO_USER_BACK:{"tag":"node","attrs":{"content-desc":"返回"},"keys":["bounds"]},
    ##用户ID 抖音号
    PAGE_FCS_VDO_USER_ID:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/l1m"},"keys":["text"]},
    ##私信按钮
    PAGE_FCS_VDO_USER_LTTR:{"tag":"node","attrs":{"text":"发私信","resource-id":"com.ss.android.ugc.aweme:id/i9p"},"keys":["bounds"]},
    ##内容输入
    PAGE_FCS_VDO_USER_LTTR_INPUT:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/fxu"},"keys":["bounds"]},
    ##发送
    PAGE_FCS_VDO_USER_LTTR_SEND:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/dpe"},"keys":["bounds"]},
    # 异常页面
    #软件更新
    PAGEERR_UPDATE_FLAG:{"tag":"node","attrs":{"text":"检测到更新","resource-id":"com.ss.android.ugc.aweme:id/jh5"}},
    PAGEERR_UPDATE_CANCEL:{"tag":"node","attrs":{"text":"以后再说","resource-id":"com.ss.android.ugc.aweme:id/elm"}}
}


""" 全局方法接口 """
def set_path_record(path):
    global lock, path_record
    lock.acquire()
    path_record = path
    lock.release()
def set_path_adb(path):
    global lock, path_adb
    lock.acquire()
    path_adb = path
    lock.release()
def set_path_tmp(path):
    global lock, path_tmp
    lock.acquire()
    path_tmp = path
    lock.release()
#固定坐标信息查询
def get_axis(name):
    global termianl_info
    axis_dict = {}
    ratio_str = ""
    for v in termianl_info:
        if v["name"] == name:
            ratio_str = v["ratio"]
            break
    ratio_obj = re.match(r"(\d+)\D+(\d+)", ratio_str)
    if not ratio_obj:
        print("Not find axis info of \"" + name + "\"")
        return axis_dict
    xmax = int(ratio_obj.group(1))
    ymax = int(ratio_obj.group(2))
    #视频主窗口
    axis = {
        PAGE_FCS_VDO_RAW_WINDOW:[
            int(xmax*1/7),
            int(ymax*3/15),
            int(xmax*5/7),
            int(ymax*10/15)]}
    axis_dict.update(axis)
    #评论窗口
    axis = {
        PAGE_FCS_VDO_CMMT_WINDOW:[
            int(xmax*1/7),
            int(ymax*6/15),
            int(xmax*5/7),
            int(ymax*13/15)]}
    axis_dict.update(axis)
    #评论中的视频窗口
    axis = {
        PAGE_FCS_VDO_CMMT_VDO_WINDOW:[
            int(xmax*1/7),
            int(ymax*1/15),
            int(xmax*5/7),
            int(ymax*3/15)]}
    axis_dict.update(axis)
    return axis_dict