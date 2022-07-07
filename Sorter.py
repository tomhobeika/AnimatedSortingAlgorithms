import tkinter as tk
import random
import time

W = 1000
H = 900
buffer = 20
nums = []
numElements = 100
numElementsInput = 0
window = tk.Tk()
winSize = "{0}x{1}".format(str(W),str(H))
rectangles = []
buttons = []
w = tk.Canvas(window, width=W, height=H - 380)
timeLabel = tk.Label(text="Real Time Taken: 0.0ms")
timeLabel.place(height=100, anchor = 'center')
timeLabel.pack(side = tk.TOP)

bigO = tk.Label(text="Average Time Complexity = ")
bigO.place(height=100, anchor = 'center')
bigO.pack(side = tk.TOP)


def setTimeLabel(totalTime):
	timeLabel['text'] = "Real Time Taken: {}ms".format(totalTime*1000)
	timeLabel.pack()
	window.update()

def setNumElements():
	numElementsInput = numElementsInputTemp.get()
	try:
		numElementsInt = int(numElementsInput)
		global numElements
		numElements = int(numElementsInput)
		
	except:
		numElementsInputTemp.set("")
		print("No int found")

	print(numElements)
	resetButton()
	window.update()
	


def setBigO(bigOText):
	bigO['text'] = "Time Complexity = {}".format(bigOText)
	bigO.pack()
	window.update()

# Bubble Sort from https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
def bubbleSort():
	bubbleSortNoGUI()
	setBigO("Θ(n^2)")
	array = nums
	greyButtons()
	n = len(array)

	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				already_sorted = False
		drawCanv()
		window.update()
		if already_sorted:
			break
	normalButtons()
	return array

def bubbleSortNoGUI():
	array = nums.copy()
	startTime = time.time()

	n = len(array)

	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				already_sorted = False
		if already_sorted:
			break
	endTime = time.time()

	totalTime = endTime - startTime
	setTimeLabel(totalTime)
	return array

# Single Bubble
def bubbleSortSingle():
	array = nums
	greyButtons()
	n = len(array)

	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				drawCanv()
				window.update()
		if already_sorted:
			break
	normalButtons()
	return array

# Insertion Sort from https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
def insertionSort():
	insertionSortNoGUI()
	setBigO("Θ(n^2)")
	greyButtons()
	array = nums
	for i in range(1, len(array)):
		window.update()
		key_item = array[i]
		j = i - 1
		while j >= 0 and array[j] > key_item:
			array[j + 1] = array[j]
			j -= 1
		drawCanv()
		
		array[j + 1] = key_item
	normalButtons()
	return array
	
def insertionSortNoGUI():
	array = nums.copy()
	startTime = time.time()

	for i in range(1, len(array)):
		key_item = array[i]
		j = i - 1
		while j >= 0 and array[j] > key_item:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key_item
	
	endTime = time.time()
	totalTime = endTime - startTime
	setTimeLabel(totalTime)
	return array
	
# Quick Sort algorithm
def quickSort():	
	greyButtons()
	setBigO("Θ(n log(n))")
	list = nums
	def sorter(items, low, high):
		drawCanv()
		if low < high:
			window.update()
			split = partition(items, low, high)
			sorter(items, low, split)
			sorter(items, split + 1, high)

	sorter(list, 0, len(list)-1)
	normalButtons()

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

def callMergeSort():
	greyButtons()
	setBigO("Θ(n log(n))")	 
	x = nums
	mergeSort(x)
	normalButtons()

# Merge Sort by Mayank Khanna	
def mergeSort(arr):
	drawCanv()
	window.update()
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2
  
		# Dividing the array elements
		L = arr[:mid]
  
		# into 2 halves
		R = arr[mid:]

		arr = R
		arr = arr + L
		  
		# Sorting the first half
		mergeSort(L)
  
		# Sorting the second half
		mergeSort(R)
  
		i = j = k = 0
  
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			drawCanv()
			window.update()	
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
			  
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
  
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def createArr():
	nums.clear()
	print(numElements)
	for x in range(numElements):
		nums.append(random.randrange(1, 100))

	print(nums)
def clearCanv():
	for x in rectangles:
		w.delete(x)
	w.pack()

def resetButton():
	createArr()
	drawCanv()

def greyButtons():
	for button in buttons:
		button["state"] = "disable"

def normalButtons():
	for button in buttons:
		button["state"] = "normal"

def drawCanv():
	clearCanv()
	tempW = W - buffer
	posX = buffer
	for x in nums:
		try:
			wCalc = 1000/numElements
			rect = w.create_rectangle(posX, 500, posX+wCalc, 50+nums[x]*2+250, fill='red')
			rectangles.append(rect)
			posX = posX + (W - buffer - buffer)/len(nums)
			w.pack()
		except:
			print("Draw Fail")
			continue


createArr()
drawCanv()

greeting = tk.Label(text="Welcome to the Algorithmic Sorting Animator!")
greeting.pack(side = tk.TOP)

# Quick Sort Button
quickSortBtn = tk.Button(window, text = 'Quick Sort', command = quickSort )
quickSortBtn.pack()

# Bubble Sort Button
bubbleSortBtn = tk.Button(window, text = 'Bubble Sort', command = bubbleSort)
bubbleSortBtn.pack()

# Bubble Sort Single Button
bubbleSortSingleBtn = tk.Button(window, text = 'Bubble Sort (Single Pass)', command = bubbleSortSingle)
bubbleSortSingleBtn.pack()

# Insertion Sort Button
insertionSortBtn = tk.Button(window, text = 'Insertion Sort', command = insertionSort)
insertionSortBtn.pack()

# Merge Sort Button
mergeSortBtn = tk.Button(window, text = 'Merge Sort (Currently Broken)', command = callMergeSort)
mergeSortBtn.pack()

# Num Elements
elementsLabel = tk.Label(text="Set Number Of Elements:")
elementsLabel.pack()

numElementsInputTemp=tk.StringVar()

numElementsBox=tk.Entry(window, textvariable = numElementsInputTemp)
numElementsBox.pack()
submitBtn = tk.Button(window, text = 'Submit', command = setNumElements)
submitBtn.pack()


# Reset Button
resetArrBtn = tk.Button(window, text = 'Reset List', command = resetButton)
resetArrBtn.pack()


buttons = [quickSortBtn, resetArrBtn, bubbleSortBtn, insertionSortBtn, bubbleSortSingleBtn, mergeSortBtn, submitBtn]
window.geometry(winSize)
window.mainloop()


