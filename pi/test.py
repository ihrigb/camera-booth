import pygame
import time
from pygame.locals import *

pygame.init()

displayinfo = pygame.display.Info()
print(displayinfo.current_w)
print(displayinfo.current_h)

WIDTH = displayinfo.current_w
HEIGHT = displayinfo.current_h
size = (WIDTH, HEIGHT)
windowSurface = pygame.display.set_mode(size, pygame.FULLSCREEN, 32)
img = pygame.image.load("images/P1120292.JPG")
img = pygame.transform.scale(img, size)
fullscreen = True
done = False
while not done:
	event = pygame.event.wait()
	if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
		if fullscreen:
			pygame.display.set_mode(size)
			fullscreen = not fullscreen
		else:
			pygame.display.set_mode(size, pygame.FULLSCREEN)
			fullscreen = not fullscreen
	if event.type == pygame.QUIT:
		done = True
		break
	windowSurface.blit(img, (0, 0))
	pygame.display.flip()

pygame.quit()

#sync.down_by_arrival(local_dir="/tmp/images", remote_dir="/DCIM/112_PANA")

#import re

#dirs = command.list_files(remote_dir="/DCIM")
#for dir in dirs:
#	print(">>> " + dir.filename)
#	if re.match(r'^[0-9]{3}_PANA$', dir.filename):
#		print(">>> >>> " + dir.filename)
#		subdir = "/DCIM/" + dir.filename
#		files = command.list_files(remote_dir=subdir)
#		for file in files:
#			print(">>> >>> >>> " + file.filename)

# monitor = sync.Monitor(local_dir="/tmp/img", remote_dir="/DCIM/112_PANA")
# monitor.sync_down()
