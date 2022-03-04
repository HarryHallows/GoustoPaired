import json


class Data:

    def __init__(self, orders, boxes):
        self.orders = orders
        self.boxes = boxes
        self.readFile = [orders, boxes]

    def readDatabase(self):

        # Reading a json file
        for item in self.readFile:
            with open(item, "r") as read_file:
                        item = json.load(read_file)
                        return print(f"{item}")   

 
    '''
    Example boilerplate code for writing to database
    def writeToDatabase(self):
        # Creating/Writing a new json file
        # Example Location : "Gousto-Interview/Data/exampleData.json"
        with open(item, "w") as write_file:
            self.readFile = json.dump(self.readFile, write_file, indent=4)
            return self.readFile
    '''
    


# INPUTS
boxes = "Gousto-Interview/Data/boxes.json"
orders = "Gousto-Interview/Data/orders.json"

# Init main class for data
data = Data(orders, boxes)
data.readDatabase() # Read json files


# TODO:
#   1)  Take these two files processes them
#   OUTPUT a list of the order ID's
#   MATCH boxes to the order ID's

#   2)  Determine the smallest possible box that the order will fit into
#   Take the sum of the CO2 footprint for each order using intelligent method
#       
#       == BOX CALCULATIONS STEPS ==
#       1. Access Box Name (eg. small, medium, large)
#       2. Access each box dimensions
#       3. Get the total volume of each box (depth * width * height)
#       4. Store each volume value

#       == ORDER CALCULATIONS STEPS ==
#       1. Access Order ID
#       2. Access for each ID the ingredients VolumeCm3
#       3. Add up each ID's total volume
#       4. Compare against box dimensions
#       - Take the sum of the CO2 footprint for each order without using intelligent method

#       == Intelligent ORDER STEPS == 
#       1. Take box volumes
#       2. Take ingredient id's volume
#       3. Add together the total order's volume for each ID
#       4. Compare with each box, IF <= box, then return true/1 
#       4.5. Else check next largest box in the list else return null/0

#       == Non-Intelligent ORDER STEPS ==
#       1. Take Largest box Volume
#       2. Compare the orders volume
#       3. return print(f"Total excess space : {box volume - orders volume}") 

