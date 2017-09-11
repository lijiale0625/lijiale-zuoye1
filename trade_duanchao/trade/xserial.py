#coding:utf-8
import serial
import time

stx = 0x03         #起始标识，固定为03
frame_count = 0x03 #帧计数器，任意设置
data_len = 0x000d    #数据长度
type = 0xe1        #E1,交易类操作命令
cmd = 0x04         #04,设备认证;01读取设备信息;02磁条卡;03获取随机数;05联机更新公钥;06工作密钥同步
len = 0x0009       #数据长度
data0 = 0x01646d46456d336541 #01对称认证,646d46456d336541 = binascii.b2a_hex('dmFEm3eA'),dmFEm3eA为客户端随机生成的8位
data = hex(int('e104000901646d46456d336541',16))     #数据
crc16 = 0x00          #CRC16循环冗余校验
ext = 0x40         #结束标识,固定为40


def device_Auth():
    pass
#0305000de104000901617a4541627879394e7840
def main():
    ser = serial.Serial(22)
    if not ser.isOpen():
        ser.open()
    print 'CTS-->',ser.getCTS()                # return the state of the CTS line
    print 'DSR-->',ser.getDSR()                # return the state of the DSR line
    print 'RI-->',ser.getRI()                 # return the state of the RI line
    print 'CD-->',ser.getCD()                 # return the state of the CD line 
    print 'portstr-->',ser.portstr
    # while(not ser.getCTS()):
        # print time.time(),'CTS-->',ser.getCTS()
        # print 'device is not ready'
        # time.sleep(1)
    # print 'device connect succ'    
        
    data = [0x02, 0x00 ,0x00, 0x05, 0xE1 ,0x03, 0x00, 0x01, 0x08, 0xEE ,0x40 ]
    #data = '0305000de104000901617a4541627879394e7840'
    #data = [0x03,0x05,0x00,0x0d,0xe1,0x04,0x00,0x09,0x01,0x61,0x7a,0x45,0x41,0x62,0x78,0x79,0x39,0x4e,0x78,0x40]
           # dmFEm3eA
           # 0305001be10400001604bc8d694d54e37a4d3ab7b8c7355f76013200001093292c40
                             # 8BF986644A4840D48E62110DA14E09BE
           # [deviceId=00210101013200001093, randomNum=dmFEm3eA, authFlag=Auto, desMessage=04bc8d694d54e37a4d3ab7b8c7355f76]
    #data = hex(int(data,16))
    print 'write-->',data
    ser.write(data)
    data = ''
    print ser.read(1).encode('hex')
    while ser.inWaiting() > 0:
        data += ser.read(1).encode('hex')
    if data != '':
        print data
    #print ser.read(8)
    ser.close()
    raw_input()
if __name__ == '__main__':
    main()