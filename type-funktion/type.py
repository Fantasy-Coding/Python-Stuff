import sys
import time
def type(message):
	print(" ")
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)
	print(" ")
