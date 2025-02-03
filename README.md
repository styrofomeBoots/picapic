# picapic

taking a photo outside of my office window to catch the changing of the seasons.

## setting up the pi

- update pi with `sudo apt update`
- install the camera module with `sudo apt install python3-picamzero`

## setting up github ssh

- run `ssh-keygen -t ed25519 -C "your-email@example.com"`
- click enter to accept default location
- ensure ssh agent is running and add the key:
  - `eval "$(ssh-agent -s)"`
  - `ssh-add ~/.ssh/id_ed25519`
  - create text file of key and add to usb: `cat ~/.ssh/id_ed25519.pub > ~/ssh_key.txt`
- On Github:
  - Navigate to: `https://github.com/settings/keys`
  - Click `New SSH key` and follow the instructions
- on the pi:
  - run `ssh -T git@github.com`

## setting up the project

- clone the repo from github
- navigate to the project directory and run:
- navigate to the project directory and setup the python environment:
  - `python -m venv venv --system-site-packages`
  - `source venv/bin/activate`
  - `pip install -r requirements.txt`

## setting up the cron

- ensure cron.sh is executable by running `chmod +x path/to/cron.sh`
- run `crontab -e`
- setup the cron by adding `30 6 * * * cd /home/path/to/project/directory && /bin/bash cron.sh >> cron.log 2>&1`
