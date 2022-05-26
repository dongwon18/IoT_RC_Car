from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
import mysql.connector
from threading import Timer, Lock
from time import sleep
import signal
import sys
from sense_hat import SenseHat
from time import sleep
import datetime
import Adafruit_DHT
import smbus
from gpiozero import LED, DistanceSensor
import RPi.GPIO as GPIO
import math


DB_IP = "aws server ip"

def closeDB(signal, frame):
    print("BYE")
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    cur.close()
    db.close()
    timer.cancel()
    timer2.cancel()
    sys.exit(0)

def polling():
    global cur, db, ready

    lock.acquire()
    cur.execute("select * from command order by time desc limit 1")
    for (id, time, cmd_string, arg_string, is_finish) in cur:
        if is_finish == 1 : break
        ready = (cmd_string, arg_string)
        cur.execute("update command set is_finish=1 where is_finish=0")

    db.commit()
    lock.release()

    global timer
    timer = Timer(0.1, polling)
    timer.start()

def MPU_Init():
        #write to sample rate register
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        #Write to power management register
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

        #Write to Configuration register
        bus.write_byte_data(Device_Address, CONFIG, 0)

        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

def sensing():
    global cur, db

    time = datetime.datetime.now()
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    humi, temp = Adafruit_DHT.read_retry(dht_sensor, DHT11)
    distance = distance_sensor.distance  # unit m

    danger_flag = 0
    if(temp < 0):
        alert_danger()
        danger_flag = 1
    if(distance < 0.1):
        alert_danger()
        danger_flag = 2

    angle_y = math.atan(-acc_x / math.sqrt(acc_y * acc_y + acc_z * acc_z)) * 180/3.14159
    angle_x = math.atan(-acc_y / math.sqrt(acc_x * acc_x + acc_z * acc_z)) * 180/3.14159

    if(abs(angle_y) < 60 or abs(angle_x) >= 30):
        alert_danger()
        danger_flag = 1


    Gx = gyro_x / 131.0
    Gy = gyro_y / 131.0
    Gz = gyro_z / 131.0
    meta_string = '0|0|0|0'
    is_finish = 0

    num1 = round(temp/100, 2)
    num2 = round(humi/100, 2)
    num3 = round(distance, 2)
    num4 = round(Gx/100, 2)
    num5 = round(Gy/100, 2)
    num6 = round(Gz/100, 2)

    meta_string = str(num4) + '|' + str(num5) + '|' + str(num6) + '|' + str(danger_flag)
    print("%f %f %f %f %f %f %d"%(num1, num2, num3, num4, num5, num6, danger_flag))
    print("%f %f"%(angle_x, angle_y))
    query = "insert into sensing(time, num1, num2, num3, meta_string, is_finish) values (%s, %s, %s, %s, %s, %s)"
    value = (time, num1, num2, num3, meta_string, is_finish)

    lock.acquire()
    cur.execute(query, value)
    db.commit()
    lock.release()

    global timer2
    timer2 = Timer(1, sensing)
    timer2.start()

def go():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.FORWARD)
    led_controll(0, 1, 0)

def back():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.BACKWARD)
    led_controll(0, 1, 0)

def stop():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.RELEASE)
    led_controll(0, 0, 0)

def left():
    pwm.setPWM(0, 0, 330)
    led_controll(0, 0, 1)

def mid():
    pwm.setPWM(0, 0, 370)

def right():
    pwm.setPWM(0, 0, 440)
    led_controll(0, 0, 1)

def led_controll(r, g, b):
    global led_r, led_g, led_b
    if(r == 0):
        led_r.off()
    else:
        led_r.on()

    if(g == 0):
        led_g.off()
    else:
        led_g.on()

    if(b == 0):
        led_b.off()
    else:
        led_b.on()

def buz_controll():
    global pwm_buz
    pwm_buz.start(50.0)
    sleep(0.5)

    pwm_buz.stop()

def alert_danger():
    led_controll(1, 0, 0)
    buz_controll()
    led_controll(0, 0, 0)

#init
db = mysql.connector.connect(host=DB_IP, user='mysql user name', password='mysql pw', database='DB name', auth_plugin='mysql_native_password')
cur = db.cursor()
ready = None
timer = None

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)
pwm = PWM(0x6F)
pwm.setPWMFreq(60)

timer2 = None
lock = Lock()

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

DHT11 = 17
LED_R = 14
LED_G = 15
LED_B = 18

ECHO = 27
TRIG = 22
BUZ = 4

bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address
MPU_Init()

dht_sensor = Adafruit_DHT.DHT11
led_r = LED(LED_R)
led_g = LED(LED_G)
led_b = LED(LED_B)
distance_sensor = DistanceSensor(ECHO, TRIG)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZ, GPIO.OUT)
GPIO.setwarnings(False)

pwm_buz = GPIO.PWM(BUZ, 262)

signal.signal(signal.SIGINT, closeDB)
polling()
sensing()

#main thread
while True:
    sleep(0.1)
    if ready == None : continue

    cmd, arg = ready
    ready = None

    if cmd == "go" : go()
    if cmd == "back" : back()
    if cmd == "stop" : stop()
    if cmd == "left" : left()
    if cmd == "mid" : mid()
    if cmd == "right" : right()
