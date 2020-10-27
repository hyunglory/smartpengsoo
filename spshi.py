
import RPi.GPIO as GPIO
import time
class hi:
    def __init__(self):
        self.pin =19
        self.pin2 = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.p2=GPIO.PWM(self.pin2,50)
        self.p= GPIO.PWM(self.pin, 50)  #PMW:펄스 폭 변조
        self.p.start(0)
        self.p2.start(0)
        self.cnt = 0
    def start(self):
        try:
            while True:
                if self.cnt == 3:
                    self.p.stop()
                    self.p2.stop()
                    break
                self.p.ChangeDutyCycle(12)
                self.p2.ChangeDutyCycle(3)
                time.sleep(0.2)
                self.p.ChangeDutyCycle(3)
                self.p2.ChangeDutyCycle(12)
                time.sleep(0.2)
                self.cnt += 1
                #p.ChangeDutyCycle(7)
                #time.sleep(0.)
                #p.ChangeDutyCycle(4)
                #time.sleep(2)
        except KeyboardInterrupt:
            self.p.stop()
            self.p2.stop()
            GPIO.cleanup()

if __name__ == "__main__":
    hi=hi()
    hi.start()
    pass
