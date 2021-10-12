import RPi.GPIO as GPIO #memasukkan module rpi
import time
pwmPin=18 #declare variable sesuai dengan pin

ledPin=23 #declare variable sesuai dengan pin

butPin=17 #declare variable sesuai dengan pin

duty=75 #declare variable sesuai dengan pin

GPIO.setmode(GPIO.BCM) #mengaktifkan nomor sistem penomoran BCM(broadcom)
GPIO.setup(ledPin,GPIO.OUT) #setup perangkat sesuai dengan pin dan menambahkan data masuk atau data keluar
GPIO.setup(pwmPin,GPIO.OUT)  #setup perangkat sesuai dengan pin dan menambahkan data masuk atau data keluar
GPIO.setup(butPin,GPIO.IN)  #setup perangkat sesuai dengan pin dan menambahkan data masuk atau data keluar
pwm=GPIO.PWM(pwmPin,200) #mempemudah kita membaca script
GPIO.output(ledPin,GPIO.LOW) #lampu dimulai dari low terlebih dahulu
pwm.start(duty) #scrpit dimulai

try:
    #membaca ketika tida ditekan
    if GPIO.input(butPin):
        pwm.ChangeDutyCycle(duty)
        GPIO.output(ledPin,GPIO.LOW)
    #jika ditekan
    else:
        #lampu menyala 
        GPIO.output(ledPin,GPIO.HIGH) 
        pwm.ChangeDutyCycle(duty)#menyesuaikan nilai output PWM lebih fleksibel
        time.sleep(0.5) #memberikan dilay
        #lampu menyala lampu mati
        GPIO.output(ledPin,GPIO.LOW)
        pwm.ChangeDutyCycle(100-duty)#menyesuaikan nilai output PWM lebih fleksibel
        time.sleep(0.5)#lampu menyala lampu mati
except KeyboardInterrupt:
    #sistem terhenti
    pwm.stop()
    #clear cache
    GPIO.cleanup()