import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('macosx')
import matplotlib.pyplot as plt

from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/accelerometer')
def echo_socket(ws):
     f=open("accelerometer.txt","a")
     plt.figure()
     data = [[0, 0, 0]]
     line1, line2, line3 = plt.plot(range(len(data)), data)
     plt.ylim(-12, 12)
     plt.ion()
     plt.show()
     while True:
        message = ws.receive()
        sys.stdout.flush()
        print(message)
        plt.pause(0.0001)
        data.append([float(i) for i in message.split(',')])
        d = np.array(data)
        d = pd.rolling_mean(d, 10)
        x = range(len(d))
        line1.set_xdata(x)
        line1.set_ydata(d[:, 0])
        line2.set_xdata(x)
        line2.set_ydata(d[:, 1])
        line3.set_xdata(x)
        line3.set_ydata(d[:, 2])
        plt.xlim(0, max(x))
        plt.draw()
        ws.send(message)
        print>>f,message
     f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
         f=open("gyroscope.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/magnetometer')
def echo_socket(ws):
         f=open("magnetometer.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/orientation')
def echo_socket(ws):
         f=open("orientation.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/stepcounter')
def echo_socket(ws):
         f=open("stepcounter.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/thermometer')
def echo_socket(ws):
         f=open("thermometer.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/lightsensor')
def echo_socket(ws):
         f=open("lightsensor.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/proximity')
def echo_socket(ws):
         f=open("proximity.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()

@sockets.route('/geolocation')
def echo_socket(ws):
         f=open("geolocation.txt","a")
         while True:
                message = ws.receive()
                print(message)
                ws.send(message)
                print>>f,message
         f.close()



@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
