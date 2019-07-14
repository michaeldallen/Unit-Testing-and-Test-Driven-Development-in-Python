import os
import json

class Prices:

    def __init__(self, prices_path):
        self.prices = {}

        if not os.path.exists(prices_path):
            raise Exception("bad path")

        with open(prices_path, "r") as prices_file:
            self.prices = json.load(prices_file)

        print("dump: {}".format(json.dumps(self.prices)))

        


    
