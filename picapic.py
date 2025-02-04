from picamzero import Camera
from datetime import date, datetime
import git
import sys
import os

def throw_error(e):
	error_time = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
	print(f"[{error_time}] ${e}")
	sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

today = date.today()
image_dir = os.path.join(SCRIPT_DIR, "pics")
image_path = os.path.join(image_dir, f"{today}.jpg")

try:
	os.makedirs(image_dir, exist_ok=True)
except Exception as e:
	throw_error(f"Directory Error: {e}")

try:
	cam = Camera()
	cam.take_photo(image_path)
except Exception as e:
	throw_error(f"Image error: {e}")

try:
	r = git.Repo(SCRIPT_DIR)
	r.git.pull()
	r.git.add(A=True)
	r.git.commit("-m", f"{today} commit")
	r.git.push()
except Exception as e:
	throw_error(f"Git error: {e}")
