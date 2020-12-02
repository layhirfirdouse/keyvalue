import json
from threading import Thread
from cachetools import TTLCache



f = open("C:/Users/pc/Desktop/new.json", "w")
#f.seek(1024 * 1024 * 1024)
class keyvalue:

    key_string_error = TypeError('Key name must be a string')
    def __init__(self, name):
        self.name=name
        self.dic={}



    def create(self):
        #Create a dictionary
        #name must be string
        if isinstance(self.name, str):
            self.dic[self.name] = {}
            return True
        else:
            raise self.key_string_error

    def add(self, name, pair):
        #Add a key-value pair to a dictionary "pair" is a tuple"
        db = TTLCache(maxsize=10, ttl=360)
        self.dic[name][pair[0]] = pair[1]
        return True

    def get(self, name, key):
        #Return the value for a key
        return self.dic[name][key]

   

    def remove(self, name, key):
        #Remove one key-value pair
        if(key not in self.dic[name]):
            print("Key does not exists")
            return 0
        value = self.dic[name][key]
        del self.dic[name][key]
        print(self.dic)
        print("Key value deleted")

    def save(self):
        json_object = json.dumps(self.dic, indent = 4) 
        f.write(json_object)
        f.close()
