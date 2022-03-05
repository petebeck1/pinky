import inkyphat
import paho.mqtt.client as mqtt
from PIL import Image, ImageFont, ImageDraw

# Set up PIL
inkyphat.set_colour('red')
w = inkyphat.WIDTH
h = inkyphat.HEIGHT
img = Image.new("P", (w, h))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/pi/TTF/Inter-Bold.ttf", 60)

def Message(msg, fg, bg):

	# Set background 
	xy = [0, 0, w, h]
	draw.rectangle(xy, bg)

	# Draw text
	mw, mh = font.getsize(msg)
	x = (w / 2) - (mw / 2)
	y = (h / 2) - (mh / 2)
	draw.text((x, y), msg, fg, font)

	# Update
	inkyphat.set_image(img)
	inkyphat.show()

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("home/onair")

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))
	cmd = msg.payload.decode().upper()
	if cmd == "BUSY":
		Message("ON AIR", inkyphat.WHITE, inkyphat.RED)
	else:
		Message("FREE", inkyphat.BLACK, inkyphat.WHITE)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.4", 1883, 60)
client.loop_forever()

