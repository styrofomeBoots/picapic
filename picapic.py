from picamzero import Camera
from datetime import date
import git
import os

today = date.today()
path = "/home/styrofomeBoots/Desktop/picapic/pics"
image_path = f"{path}/{today}.jpg"

if not os.path.exists(path):
	os.makedirs(path)

cam = Camera()
cam.start_preview()
cam.take_photo(image_path)
cam.stop_preview()

r = git.Repo()
r.git.pull()
r.git.add(u=True)
r.git.commit(f"-m'{today} commit'")
r.git.push()
