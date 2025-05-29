from picamzero import Camera # type: ignore
import logging
from datetime import date, datetime
import git
import sys
import os

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def throw_error(msg):
	logging.error(msg)
	sys.exit(1)

def take_photo(script_dir, today):
	image_dir = os.path.join(script_dir, "pics")
	image_path = os.path.join(image_dir, f"{today}.jpg")

	try:
		os.makedirs(image_dir, exist_ok=True)
	except OSError as e:
		throw_error(f"Directory Error: {e}")

	try:
		cam = Camera()
		cam.take_photo(image_path)
	except Exception as e:
		throw_error(f"Image error: {e}")
	return

def commit_changes_if_friday(script_dir, today):
	if today.weekday() != 4:
		logging.info("Today is not Friday; skipping Git commit.")

	try:
		repo = git.Repo(script_dir)
		origin = repo.remote(name='origin')

		origin.pull()
		logging.info("Pulled latest changes from remote.")

		repo.git.add(A=True)
		if repo.is_dirty(index=True, working_tree=False, untracked_files=True):
			repo.git.commit("-m", f"{today} commit")
			repo.git.push()
			logging.info("Pushed committed changes to remote repo.")
		else:
			logging.info("No changes to commit.")
	
	except git.GitCommandError as e:
		throw_error(f"Git operation failed: {e}")
	except Exception as e:
		throw_error(f"Unexpected error during Git operations: {e}")

def main():
	script_dir = os.path.dirname(os.path.abspath(__file__))
	today = date.today()
	os.chdir(script_dir)
	take_photo(script_dir, today)
	commit_changes_if_friday(script_dir, today)

if __name__ == "__main__":
	main()