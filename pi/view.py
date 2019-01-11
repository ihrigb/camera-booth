import logging
import sys
import threading
import time

import pygame
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Viewer:

	def __init__(self, fullscreen = True):
		self._fullscreen = fullscreen
		pygame.init()
		displayinfo = pygame.display.Info()
		self._size = (displayinfo.current_w, displayinfo.current_h)
		self._window_surface = pygame.display.set_mode(self._size, pygame.FULLSCREEN, 32)

	def run(self):
		done = False
		while not done:
			event = pygame.event.wait()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
				if self._fullscreen:
					pygame.display.set_mode(self._size)
					self._fullscreen = not self._fullscreen
				else:
					pygame.display.set_mode(self._size, pygame.FULLSCREEN)
					self._fullscreen = not self._fullscreen
			if event.type == pygame.QUIT:
				done = True

		pygame.quit()


	def update(self, src_path):
		try:
			img = pygame.transform.scale(pygame.image.load(src_path), self._size)
			self._window_surface.blit(img, (0, 0))
			pygame.display.flip()
		except:
			logging.error("Displaying a new image failed.")

class ViewFileSystemEventHandler(FileSystemEventHandler):

	def __init__(self, viewer):
		self._viewer = viewer

	def on_created(self, event):
		self.event(event)

	def on_modified(self, event):
		self.event(event)

	def event(self, event):
		if event.is_directory:
			return
		self._viewer.update(event.src_path)


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	path = sys.argv[1] if len(sys.argv) > 1 else '.'
	viewer = Viewer()
	event_handler = ViewFileSystemEventHandler(viewer)

	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	viewer.run()
	observer.stop()
	observer.join()
