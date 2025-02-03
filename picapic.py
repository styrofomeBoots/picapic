from picamzero import Camera
from datetime import date
import os

path = "/home/styrofomeBoots/Desktop/picapic/pics"
image_path = f"{path}/{date.today()}.jpg"

if not os.path.exists(path):
	os.makedirs(path)

cam = Camera()
cam.start_preview()
cam.take_photo(image_path)
cam.stop_preview()