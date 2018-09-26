import os
import re
import gzip
import time

class Log(object):
    '一条日志'
    def __init__(self, line):
        '初始化时用一行日志 字符串'
        # arr:[ip, time, url, num1num2, ?, phone]
        self.line = line
        arr = re.findall('(.*) - - \[(.*)\] "(.*)" (.*) "(.*)" "(.*)"', line)[0]
        self.ip = arr[0]
        self.datetime = arr[1]
        self.method = arr[2].split(' ')[0]
        self.url = arr[2].split(' ')[1]


    def Print(self):
        print('ip:\t', self.ip)
        print('date:\t', self.datetime)
        print('url:\t', self.url)
        print('-'*20, end='\n\n')


    def test(self):
        arr = re.findall('(.*) - - \[(.*)\] "(.*)" (.*) "(.*)" "(.*)"', self.line)[0]
        print(arr[-1])
        

def eachLine():
    '输出一行日志的迭代器'
    for filename in [os.listdir('nginx')[0]]:
        with gzip.open('nginx/access.log.2.gz', 'rb') as file:
            for index,line in enumerate(file.readlines()):
                yield index,str(line, encoding='utf-8').strip()


if __name__ == '__main__':
    for index,line in eachLine():
        log = Log(line)
        print(index)
        log.test()
        print()
        time.sleep(1);
