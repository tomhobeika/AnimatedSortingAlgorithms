import tkinter as tk
import random

W = 1000
H = 800
buffer = 20
nums = []
numElements = 100
window = tk.Tk()
winSize = "{0}x{1}".format(str(W),str(H))
rectangles = []
w = tk.Canvas(window, width=W, height=H)

# Quick Sort algorithm to sort the list by count of word
def quickSort():
	list = nums
	def sorter(items, low, high):
		drawArr()
		if low < high:
			split = partition(items, low, high)
			sorter(items, low, split)
			sorter(items, split + 1, high)

	sorter(list, 0, len(list)-1)

	

# Partition method used for Quick Sort to get pivot point
def partition(list,start,end):
	low = start - 1
	high = end + 1

	pivot = list[(low + high) // 2]
	
	while True:
		low = low + 1
		while list[low] < pivot:
			low = low + 1

		high = high - 1
		while list[high] > pivot:
			high = high - 1

		if low >= high:
			return high

		list[low], list[high] = list[high], list[low]

		clearCanv()


def createArr():
	for x in range(numElements):
		nums.append(random.randrange(1, 100))
def clearCanv():
	for x in rectangles:
		w.delete(x)
	w.pack()
def drawArr():
	tempW = W - buffer
	posX = buffer
	for x in nums:
		try:
			rect = w.create_rectangle(posX, 500, posX+10, 50+nums[x]*2+250,fill='red')
			rectangles.append(rect)
			posX = posX + (W - buffer - buffer)/len(nums)
			w.pack()
		except:
			continue
		
createArr()
drawArr()

window.geometry(winSize)

greeting = tk.Label(text="Welcome to the Algorithmic Sorting Animator!")
greeting.pack(side = tk.TOP)


# Create a Button
btn = tk.Button(window, text = 'Quick Sort', command = quickSort)
btn.pack()

window.mainloop()


