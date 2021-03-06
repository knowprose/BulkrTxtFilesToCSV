#Copyright Taran Rampersad, 2016-

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License

#TODOs show where you should edit for your own local directory. 

# Use: Requires you to have Python on your system (tested with 3.5). Drop this in the appropriate directory, change path accordingly (see TODOs). Run it. 

import os
import csv

# Get the text file names in the directory. 
dirTxtListing = os.listdir("D:/FlickrImages")
myPath = 'D:/FlickrImages' #TODO Change this to the path where the txt files are (with the jpgs)
myCsvOutput = 'flickr.csv' #TODO Change this filename to one that you want. Or not. 
metadataFiles = []
for item in dirTxtListing:
	if ".txt" in item: 
		metadataFiles.append(myPath+'/'+item) 
with open(myCsvOutput, 'w', newline='') as csvfile: 
	photoinfowriter = csv.writer(csvfile, delimiter=',')
	#First row to be warm and fuzzy.
	row = ['Photographer','Photo URL','License','Taken Date','Upload Date','Views','Comments','Title','Description','Tags']
	photoinfowriter.writerow(row)
	#pull data from individual metadata Files and insert into csv file
	for singleFile in metadataFiles:
		a = open(singleFile,"r")
		inLineCount = 0
		row = []
		with open(singleFile) as fin:
			for line in fin:
				inLineCount +=1
				if inLineCount == 10:
					photographer = line[15:-1]
				if inLineCount == 11:
					url= line[15:-1]
				if inLineCount == 12:
					license=  line[15:-1]
				if inLineCount == 13:
					taken= line[15:-1]
				if inLineCount == 14:
					uploaded=  line[15:-1]
				if inLineCount == 15:
					views =  line[15:-1]
				if inLineCount == 16:
					comments =  line[15:-1]
				if inLineCount == 22:
					title =  line[0:-1]
				if inLineCount == 28:
					description=  line[0:-1]
				if inLineCount == 34:
					tags=  line[0:-1]
		row = [photographer, url, license, taken, uploaded, views, comments, title, description, tags]
		photoinfowriter.writerow(row)



