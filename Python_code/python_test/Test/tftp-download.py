# -*- coding:utf-8 -*-
#需要开启防火墙，不然responseData = udpSocket.recvfrom(1024)这里会一直阻塞
import struct
from socket import *
import time
import os

downloadFileName = raw_input("请输入要下载的文件名：")
requestFileData = struct.pack("!H%dsb5sb"%len(downloadFileName), 1, downloadFileName, 0, "octet", 0)
print "requestFileData = ", requestFileData
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(requestFileData, ("192.168.6.68", 69))

flag = True
num = 0
f = open(downloadFileName, "w")

while True:
	print "---1---"
	responseData = udpSocket.recvfrom(1024)
	print "---2---"
	recvData, serverInfo = responseData

	opNum = struct.unpack("!H", recvData[:2])

	packetNum = struct.unpack("!H", recvData[2:4])

	print(packetNum[0])

	# print("opNum=%d"%opNum)
	# print(opNum)

	# if 如果服务器发送过来的是文件的内容的话:
	if opNum[0] == 3:  # 因为opNum此时是一个元组(3,)，所以需要使用下标来提取某个数据


		# 计算出这次应该接收到的文件的序号值，应该是上一次接收到的值的基础上+1
		num = num + 1

		# 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
		# 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
		if num == 65536:
			num = 0

		# 判断这次接收到的数据的包编号是否是 上一次的包编号的下一个
		# 如果是才会写入到文件中，否则不能写入（因为会重复）
		if num == packetNum[0]:
			# 把收到的数据写入到文件中
			f.write(recvData[4:])
			num = packetNum[0]

		# 整理ACK的数据包
		ackData = struct.pack("!HH", 4, packetNum[0])
		udpSocket.sendto(ackData, serverInfo)

	elif opNum[0] == 5:
		print("sorry，没有这个文件....")
		flag = False

	# time.sleep(0.1)

	if len(recvData) < 516:
		break

if flag == True:
	f.close()
else:
	os.unlink(downloadFileName)  # 如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除
