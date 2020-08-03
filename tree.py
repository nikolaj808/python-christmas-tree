import os
import sys
import threading
import random
import time

mutex = threading.Lock()
tree = list(open("tree.txt").read().rstrip())

yellow = []
red = []
green = []
blue = []

def dot(color):
	if color == 'yellow':
		return '\u001b[33m•\u001b[0m'
	if color == 'red':
		return  '\u001b[31m•\u001b[0m'
	if color == 'green':
		return '\u001b[32m•\u001b[0m'
	if color == 'blue':
		return '\u001b[34m•\u001b[0m'

def lights(color, lightList):
	off = True
	while True:
		for light in lightList:
			tree[light] = dot(color) if off else '•'

		mutex.acquire()
		os.system('clear')
		print(''.join(tree))
		mutex.release()

		off = not off

		time.sleep(random.uniform(0.5, 1.25))

for i, c in enumerate(tree):
	if c == 'Y':
		yellow.append(i)
		tree[i] = '•'
	if c == 'R':
		red.append(i)
		tree[i] = '•'
	if c == 'G':
		green.append(i)
		tree[i] = '•'
	if c == 'B':
		blue.append(i)
		tree[i] = '•'

thread_y = threading.Thread(target=lights, args=('yellow', yellow))
thread_r = threading.Thread(target=lights, args=('red', red))
thread_g = threading.Thread(target=lights, args=('green', green))
thread_b = threading.Thread(target=lights, args=('blue', blue))

thread_y.start()
thread_r.start()
thread_g.start()
thread_b.start()

thread_y.join()
thread_r.join()
thread_g.join()
thread_b.join()