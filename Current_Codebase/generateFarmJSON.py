from asyncio.windows_events import NULL
from email.policy import default
import json
import csv

# Farm class
class Farm:
        def __init__(self, name, lat, lng, url=NULL):
                self.name = name
                self.latitude = lat
                self.longitude = lng
                self.farmData = {}
                if (url):
                        self.url = url
                else:
                        self.url = NULL
        
        # print all values of the class for debugging purposes
        def __repr__(self):
                farm = str(self.name) + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.farmData) + "\n\n\n"
                return farm

# A bad way of making list for coords
# NOTE: New farm coordinate entries must be appended
# in the order they appear within the csv file
# Make sure to delete rows (farms) from the csv which are not included
# for example: farms where you couldn't verify ownership (and prove it's still a century farm)
aList = []
aList.append(Farm("Reynolds Farms",
        44.612636, 
        -123.214536))
aList.append(Farm("Garland Nursery",
        44.624781, 
        -123.207734))
aList.append(Farm("Scharf Family Farm",
        45.038913, 
        -123.235096))
aList.append(Farm("Fiala Farms",
        45.371628, 
        -122.690767,
        "https://lh3.googleusercontent.com/pw/AM-JKLVjJ7Dbi05YTz4eR1nC7Ptb9v71pLFWejg--Pr6axj24yOa_uo21w3B1DBvcCYRY17XGUkp0rfym7vTcEQnlzIBoVg0LD52YbJxlXWe1sSiIWb_0SamPTDTRfr7ivzeo7Ba4AyLVYFabZsRcVDl0r6V=w703-h937-no?authuser=0"))
aList.append(Farm("Harnisch Farms",
        44.721034, 
        -123.074716))
aList.append(Farm("Chambers Farm",
        44.6488167,
        -123.0253000))
aList.append(Farm("Gordon Zimmerman Farm",
         45.324885, 
        -123.177172))
aList.append(Farm("Bruck Farm",
        45.30645295190772,
        -122.7278229261364))
aList.append(Farm("Freeman Family Farm",
        45.16480057879585,
        -123.2787515562552))
aList.append(Farm("Jack Vaughan Farm",
         45.171955, 
        -122.553226))
aList.append(Farm("MacFarlane Farm",
         45.369959, 
        -122.492875))
aList.append(Farm("McKay Farms, Inc.",
         45.196182, 
        -122.936665))
aList.append(Farm("Jackson-Martinak Farm",
         44.544599, 
        -123.046902))
aList.append(Farm("Rice Ranch",
         44.339541, 
        -122.770838))
aList.append(Farm("Richardson Farm",
         44.129742, 
        -123.302477))
aList.append(Farm("Silver Mountain Enterprises, LLC",
         44.882534, 
        -122.718024))
aList.append(Farm("Goodrich Farm",
         45.185201, 
        -123.118728))
aList.append(Farm("Hawley Land & Cattle Co.",
         43.754222, 
        -123.115768))
aList.append(Farm("Montgomery Homestead Farm",
         44.732773, 
        -122.768135))
aList.append(Farm("Buzz Mitchell Farms",
         44.568474, 
        -122.912520))
aList.append(Farm("Bryon Scott Farms, Inc.",
         44.522564, 
        -123.111921))
aList.append(Farm("Bierly Farm",
         44.323703, 
        -123.056517))
aList.append(Farm("Fanning Farms",
         45.070975, 
        -123.296363))
aList.append(Farm("Hiebenthal Farms",
         45.002677, 
        -123.299946))
aList.append(Farm("McPhillips Farms Inc",
         45.163932, 
        -123.237324))
aList.append(Farm("Payne Farms",
         45.260040, 
        -123.157239))
aList.append(Farm("Sam Luethe Farm",
         45.605375, 
        -122.838158))
aList.append(Farm("AJ Strubhar Farm ",
         45.184137, 
        -122.765053))
aList.append(Farm("Duck Inn Group, LLC",
         45.092563, 
        -122.904082))
aList.append(Farm("Three Oaks Farm",
         45.200157, 
        -123.116015))
aList.append(Farm("VanDomelen Family Farm",
         45.626693, 
        -123.038364))
aList.append(Farm("Batchelder Farms, LLC",
         45.589162, 
        -122.947361))
aList.append(Farm("Three Branches, LLC",
         45.341602, 
        -123.226414))
aList.append(Farm("Jansen Farm",
         45.554103, 
        -123.084298))
aList.append(Farm("Plagmann Farms, Inc.",
         44.657283, 
        -122.951597))
aList.append(Farm("Two Fox Farm",
         45.049030, 
        -123.202956,
        "https://lh3.googleusercontent.com/pw/AM-JKLXEFg_paGnsS2YZUEvIZfmVhemTCWYGStWhTulba3bR4YvvmGk5jFFyw9mis-2-h0xmXKNPfWwpZPbXj1T6iYTUPsWCmJqHQ6P-J9lNjgB4ESp9Sh036tiz0s3IfgFb6iq7Mddqp7du-J2nr8OAkWOW=w703-h937-no?authuser=0"))
aList.append(Farm("Charles Ludwig Falk Farm",
         44.372268, 
        -123.078142))
aList.append(Farm("Louis R. & Anna Falk Farm",
         44.362760, 
        -123.056456))
aList.append(Farm("Hynes Farm",
         45.050123, 
        -122.867596))
aList.append(Farm("Fisher Patterson",
         44.895447, 
        -122.777044))
aList.append(Farm("Taghon Farm",
         45.532212, 
        -123.060562))
aList.append(Farm("Christensen Farm",
         44.280888, 
        -123.070421))
aList.append(Farm("Gentleacres/Orion Farms",
         44.860827, 
        -123.237205))
aList.append(Farm("Mid Valley Farm",
         45.416350, 
        -122.900065))
aList.append(Farm("Smith Bros. Farms, LLC",
         44.522904, 
        -123.207757))
aList.append(Farm("Jesse & Ruby Looney Farm",
         44.753588, 
        -123.016446))
aList.append(Farm("Maple Hill Farm",
         45.075112, 
        -122.840758))
aList.append(Farm("Mosby Century Farm",
         43.781987, 
        -122.998386))
aList.append(Farm("Alder Glade Farm",
         44.980899, 
        -122.770134))
aList.append(Farm("M. Christensen Family Farm, LLC",
         45.133789, 
        -123.271508))
aList.append(Farm("Peter Fred Gossen Farm",
         45.590375, 
        -122.908860))
aList.append(Farm("Iwasaki Bros. Inc.",
         45.501292, 
        -122.966665))
aList.append(Farm("The Misner Family Farm",
         44.634869, 
        -122.906599,
        "https://lh3.googleusercontent.com/pw/AM-JKLWoivHhYk60ZeitgOcogoxKtR6gVznXLaFFoiq5P9mclELoWWvj4ZQlCbMxaLj5rkPKTostOrS5g1Ivq77Ivr6HtzjEYHaFlmgieyvIZgV6kIhn4l6DHfT_ygNaWeDTWMcKY-Qx8pQc7ohwmvbe9jOw=w703-h937-no?authuser=0"))
aList.append(Farm("Cattrall Brothers Vineyards",
         45.090944, 
        -123.162414))
aList.append(Farm("Basil & Mary Stupfel",
         45.198436, 
        -122.984627))
aList.append(Farm("Haslebacher Farms",
         45.019848, 
        -122.908823))
aList.append(Farm("Herring Farm",
         45.311883, 
        -123.020690))
aList.append(Farm("Four Ridge Orchards",
         45.424348, 
        -123.007318))
aList.append(Farm("Oak Creek Farm",
         44.478520, 
        -122.880605))
aList.append(Farm("Bar M Ranch",
         44.472232, 
        -123.099577))
aList.append(Farm("Shady Brook Farm",
         45.237954, 
        -123.102738))
aList.append(Farm("Haskin Heritage Century Farm", 
        44.50858650097742, 
        -122.8656571641482))
aList.append(Farm("Voss Farms", 
        45.344336121,    
        -122.828323358))
aList.append(Farm("Mullen Farms",
        45.228131241,	
        -122.989806315))
aList.append(Farm("Tideman Johnson Farm", 
        45.463380202,   
        -122.623511914))
aList.append(Farm("Select Seed Promised Seed",
        45.11056587439315, 
        -123.2682577145877))
aList.append(Farm("Delano Farms",
        45.34976602696314, 
        -122.4906612610669))
aList.append(Farm("The Beitel Farm",
        44.8278554054365, 
        -122.7628299775307))
# start adding more farms to the list here
# farm names are often (but not always) included in the csv file
# consider integrating longitude and latitude into farmData
# to avoid the use of child objects
# will require changing some of the for loop below 


# Parse OSFRP data
with open('farms.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)        
        reader = list(reader)
        for idx, row in zip(aList, reader):
                idx.farmData = row
                
# Convert to JSON
jsonString = json.dumps(aList, default= lambda x: x.__dict__)
jsonFile = open("farms.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
