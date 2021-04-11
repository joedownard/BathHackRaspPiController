import socketio
import RPi.GPIO as GPIO

sio = socketio.Client()

sio.connect('http://192.168.0.161:5000')
sio.emit('ignoreme', 'ignoreme')
print('CONNECTED! my sid is', sio.sid)


def F():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    return "success!"


def F_OFF():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    return "success!"


def R():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    return "success!"


def R_OFF():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    return "success!"


def L():
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    return "success!"


def L_OFF():
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    return "success!"


def B():
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    return "success!"


def B_OFF():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    return "success!"


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

@sio.on("clear")
def clear(data):
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)


@sio.on("move")
def move(data):
    exec(data['data'] + "()")
