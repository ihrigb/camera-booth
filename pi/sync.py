from tfatool import sync
import re
import sys
import time

is_running = True
filter_jpg = lambda f: f.filename.lower().endswith(".jpg")

while is_running:
	try:
		print("GO")
		monitor = sync.Monitor(filter_jpg, local_dir="images", remote_dir="/DCIM/112_PANA")
		monitor.sync_down()
		monitor.join()
	except KeyboardInterrupt:
		print("Received KeyboardInterrupt.")
		is_running = False
	except:
		print("Exception while syncing")
		try:
			time.sleep(5000)
		except KeyboardInterrupt:
			is_running = False
monitor.stop()
monitor.join()
sys.exit(0)
