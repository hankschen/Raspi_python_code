import sys
import urllib
# import PRi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib2


def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))


# main() function
def main():
    # use sys.argv if needed(檢查使用者執行程式時是否有輸入key)
    if len(sys.argv) < 2:
        print('Usage:python tstest.py PRIVATE_KEY')
        exit(0)
    print 'starting....'
    baseURL = "https://api.thingspeak.com/update?api_key=%s" % sys.argv[1]


print baseURL

while True:
    try:
        RH, T = getSensorData()
        print RH
        print T
        f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T))
        print f.read()  # 印出回傳值
        f.close()  # 關掉網路
        sleep(10)
    except:
        print "exiting."
        break  # call main
if __name__ == '__main__':
    main()
