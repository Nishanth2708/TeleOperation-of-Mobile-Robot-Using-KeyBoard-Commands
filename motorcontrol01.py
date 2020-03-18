import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31,gpio.OUT)
    gpio.setup(33,gpio.OUT)
    gpio.setup(35,gpio.OUT)
    gpio.setup(37,gpio.OUT)

def gameover():
    #set all pins low
    gpio.output(31,False)
    gpio.output(33,False)
    gpio.output(35,False)
    gpio.output(37,False)

def forward(tf):
    init()
    #left wheel 
    gpio.output(31,True)
    gpio.output(33,False)
    
    #right wheel 
    gpio.output(37,True)
    gpio.output(35,False)

    #weight
    time.sleep(tf)

    #send alkl pins  and cleanup
    gameover()
    gpio.cleanup()
    


forward(2)


