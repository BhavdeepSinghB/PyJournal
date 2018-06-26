import datetime

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
		file = open("Journal.txt", 'a')
		file.write('[' + str(self.timestamp) + ']')
		file.write("\n")
		file.write(self.textentry)
		file.write("\n\n\n")

entries = []

def main():
	choice = '1'
	while(choice != 'Q' or choice !='q'):
		print("------------------------------------")
		print("Welcome to XDiary 2.0")
		print("Please choose an option to continue")
		print("1-Write to Journal")
		print("2-Read entries of a particular date")
		print("3-Read whole Journal")
		print("4-About")
		print("Q-Quit")

		choice = raw_input()

		if(choice == "1"):
			write()
		elif(choice == "3"):
			read()
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
	rfile = open("Journal.txt", "r")
	readstuff = rfile.readlines()
	#print(readstuff)
	r = iter(readstuff)
	init = next(r)
	date1 = init[1:11] 
	tail = next(r)
	date2 = tail[1:11]
	
	try:
		while(userDate != date1):
			init = next(r)
			date1 = init[1:11] 
		tail = next(r)
		date2 = tail[1:11]	
		if(userDate == date1):
			date2 = printJournal(init, tail, r)
			while(date1 == date2):
				tail = next(r)
				date2 = printJournal(init, tail, r)
	except StopIteration:
		print("Date not found")



def printJournal(init, tail, r):
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

def updateLogs():
	#logfile 
	print("Ending")

main()


