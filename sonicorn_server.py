import unicornhat as unicorn
import time, colorsys
import numpy as np


def make_gaussian(fwhm):
	x = np.arange(0, 8, 1, float)
	y = x[:, np.newaxis]
	x0, y0 = 3.5, 3.5
	fwhm = fwhm
	gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
	return gauss

def pulse_rainbow():
	for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
		fwhm = 5.0/z
		gauss = make_gaussian(fwhm)
                start = time.time()
		for y in range(8):
			for x in range(8):
				h = 1.0/(x + y + 1)
				s = 0.8
				v = gauss[x,y]
				rgb = colorsys.hsv_to_rgb(h, s, v)
				r = int(rgb[0]*255.0)
				g = int(rgb[1]*255.0)
				b = int(rgb[2]*255.0)
				unicorn.set_pixel(x, y, r, g, b)
		unicorn.show()
                end = time.time()
                t = end - start
                if t < 0.04:
		    time.sleep(0.04 - t)

pulse_rainbow()

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
	pulse_rainbow()

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()


