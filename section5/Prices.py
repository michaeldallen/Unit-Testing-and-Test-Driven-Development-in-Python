import os
import json

class Prices:

    def __init__(self, prices_path):
        self.prices = {}

        if not os.path.exists(prices_path):
            raise Exception("bad path")

        prices_file = open(prices_path, "r")
        self.prices = json.load(prices_file)
        data_string = json.dumps(self.prices)
        print("dump: {}".format(data_string))

        


    
