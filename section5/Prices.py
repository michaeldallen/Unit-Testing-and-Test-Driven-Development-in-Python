import os
import json

class Prices:

    def __init__(self, prices_path):
        self.prices = {}

        if not os.path.exists(prices_path):
            raise Exception("no such path: {}".format(prices_path))

        with open(prices_path, "r") as prices_file:
            self.prices = json.load(prices_file)

        s = json.dumps(self.prices)


    def __iter__(self):

        s = json.dumps(self.prices)
        for s2 in self.prices:
            yield s2, self.prices[s2]


    def dump(self):
        for foo in self:
            print("  {}".format(foo))
