#!/usr/bin/python
#coding=utf-8
'''
Created on 2015-8-4
@author: Administrator
'''

import threading,subprocess
from time import ctime,sleep,time
import Queue
from sys import argv

# dir_name = argv[1]
dir_name = '_anhui'
q=Queue.Queue()
class ThreadUrl(threading.Thread):
    def __init__(self,q,output_name):
        threading.Thread.__init__(self)
        self.q=q
        self.f_name = output_name


    def run(self):
        while True:
            host=self.q.get()
            ret=subprocess.call('ping -c 1 -w 1 '+host,shell=True,stdout=open(self.f_name,'a'))
            # if ret:
                # print(host +" is down")
            # else:
                # print(host + " is up")
            self.q.task_done()
            # print ret.communicate()



def main(ip_s):
    for i in range(150):
        t=ThreadUrl(q,'res' + dir_name + '/' + str(i) + '.txt')
        t.setDaemon(True)
        t.start()
    for host in ip_s:
        q.put(host)
    q.join()



f = open("ip" + dir_name +".txt", 'r')
for line in f.readlines():
    ip_sum = []
    line = line.strip()
    ipline = line.split(' ')
    print(ipline[0])
    print(ipline[1])
    str1list = ipline[0].split('.')
    str2list = ipline[1].split('.')
    start = 0
    for i in range(len(str1list)):
        if str(str1list[i]) != str(str2list[i]):
            start = i
            break
    # print start
    if start == 1:
        for i in range(int(str1list[1]), (int(str2list[1])+1)):
            for i2 in range(256):
                for i3 in range(256):
                    temp_ip = str(str1list[0]) + '.' + str(i) + '.' + str(i2) + '.' + str(i3)
                    ip_sum.append(temp_ip)
    else:
        for i in range(int(str1list[2]), (int(str2list[2]) + 1)):
            for i2 in range(256):
                temp_ip = str(str1list[0]) + '.' + str(str1list[1]) + '.' + str(i) + '.' + str(i2)
                ip_sum.append(temp_ip)

    start = time()
    main(ip_sum)
    print "Elasped Time:%s" % (time()-start)
f.close()