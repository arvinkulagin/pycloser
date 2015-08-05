import signal
import sys

EXIT_CODE_OK = 0

class Stack(object):
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			return None

	def is_empty(self):
		return self.items == []

class Closer(object):
	def __init__(self):
		self.handlers = Stack()

	def _signal_handler(self, signal, frame):
		self.close()
	
	def defer(self, handler):
		self.handlers.push(handler)

	def listen(self):
		signal.signal(signal.SIGINT, self._signal_handler)
		signal.signal(signal.SIGTERM, self._signal_handler)
		signal.signal(signal.SIGHUP, self._signal_handler)

	def close(self):
		while not self.handlers.is_empty():
			func = self.handlers.pop()
			func()
		sys.exit(EXIT_CODE_OK)

_closer = Closer()

def defer(handler):
	_closer.defer(handler)

def listen():
	_closer.listen()

def close():
	_closer.close()