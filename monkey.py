# -*- coding: UTF-8 -*-

# @Time    : 2018/3/20 下午6:42
# @Author  : lily
# @File    : monkey.py
# @PROJECT_NAME : Pythoncoding

import os


class AdbCommand(object):

    def call_adb(self,command):
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

# 检查已连接的设备
    def attached_devices(self):
        result = self.call_adb('devices')
        device = result.partition('\n')[2].split('\t')[0]
        return device

# 获取设备id
    def get_devices(self):
        print(self.attached_devices())

# 将手机文件拷贝电脑中
    def pull(self,remote,local):
        result = os.system("adb pull %s %s" %(remote,local))
        return result
# 将电脑文件拷贝到手机
    def push(self,local,remote):
        os.system("adb push %s %s" % (local,remote))


# 录制屏幕
    def screenrecord(self,remote,local,time):
        os.system("adb shell screenrecord --time-limit %d %s " % (time,remote))
        self.pull(remote,local)


# 截屏
    def screencap(self,local,remote):
        os.system("adb shell /system/bin/screencap -p %s" % remote)
        self.pull(remote,local)


if __name__ == '__main__':
    adb = AdbCommand()
    adb.get_devices()
    adb.screencap('/Users/abc','/sdcard/demo1.png')

