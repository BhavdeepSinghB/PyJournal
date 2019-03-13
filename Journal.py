import datetime

#Edit these
fileName = "BuildLog.txt"						
filePath = "../100DaysOfCode/Timer/"			

fileFinder = filePath + fileName


class entry:
	timestamp = datetime.datetime.now()
	textentry = "\n"
	time = datetime.time()
	date = datetime.date.today()

	def setText(self, text):
		self.textentry = text

	def getText(self):
		return self.textentry

	def getTimeStamp(self):
		return self.timestamp

	def getDate(self):
		return str(self.date)

	def makePermanent(self):
		file = open(fileFinder, 'a')			#Change this to whatever file you want to write to, by default its set to the testing file
		file.write('[' + str(self.timestamp) + ']')
		file.write("\n")
		file.write(self.textentry)
		file.write("\n\n\n")

entries = []

def main():
	choice = '1'
	while(choice != 'Q' or choice !='q'):
		print("------------------------------------")
		print("Welcome to PyJournal")
		print("Please choose an option to continue")
		print("1-Write to Journal")
		print("2-Read entries of a particular date")
		print("3-Read whole Journal")
		print("4-About")
		print("Q-Quit")

		choice = raw_input()

		if(choice == "1"):
			write()
		elif(choice == "2"):
			read()
		elif(choice == "3"):
			printJournal()
		elif(choice == 'Q' or choice=='q'):
			updateLogs()
			break
		else:
			print("Testing")

	

def write():
	textThis = entry()
	print(textThis.getTimeStamp())
	print("Entry: ")
	myText = []
	while True:
		line =  raw_input()
		if line:
			myText.append(line)
		else:
			break
	combinedText = "\n".join(myText)
	textThis.setText(combinedText)
	
	saveQuestion = raw_input("Save? [Y/N] ")
	if(saveQuestion == "Y" or saveQuestion == "y"):
		textThis.makePermanent()
	entries.append(textThis)
	del textThis

def read():
	flag = False
	userDate = raw_input("Enter a date (yyyy-mm-dd) ")
	rfile = open(fileFinder, "r")
	readstuff = rfile.readlines()
	r = iter(readstuff)
	init = next(r)
	date1 = init[1:11] 
	tail = next(r)
	date2 = tail[1:11]
	

	try:
		while(userDate != date1):
			init = next(r)
			date1 = init[1:11] 
		#tail = next(r)
		#date2 = tail[1:11]	
		if(userDate == date1):
			date2 = printJournalByDate(init, tail, r)
			while(date1 == date2):
				tail = next(r)
				date2 = printJournalByDate(init, tail, r)
	except StopIteration:
		print("Date not found")



def printJournalByDate(init, tail, r):
	try:
		while(init[0] != tail[0]):
			print(tail)
			tail = next(r)
			date2 = tail[1:11]
	except StopIteration:
		pass
	finally:
		del r
		return date2

def printJournal():
	rfile = open(fileFinder, "r")
	print(rfile.read())

def updateLogs():
	#logfile 
	print("Ending")

main()



