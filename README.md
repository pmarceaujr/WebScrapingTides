# WebScrapingTides

Python code to scrape a web page for low tides for a specified list of beaches. The data returned will be the times of the low tides during the daylight hours.

# Installation:

- clone the repo: https://github.com/pmarceaujr/WebScrapingTides
- cd into the repo directory
- install the required modules: pip install -r requirements.txt

# Running the program:

- The what_beaches.txt file in the data directory will be used to provide the list of beaches.
- Enter one beach per line.
- execute the program by typing: python .\show_low_tide.py

# ToDo:

- currently the output is all low tides for a single beach (Half-Moon-Bay-California)
- I still need to add a loop for the file read to loop through all beaches listed in the input file
- still need to figure out the string to time object conversion so I can filter out and display only low tides during daylight hours
- refactor the code so there is a function for opening, reading, formatting the input data and writing it to a list and pass the list to the main function for scraping
- create a main function to handle the looping through the list of beaches
- create a json file with the name of the beach and the daylight low tides for that beach.
- build a web UI using flask to display the data
