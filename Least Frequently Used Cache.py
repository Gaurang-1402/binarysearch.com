# approach
# watch this: https://www.youtube.com/watch?v=Jn4mbZVkeik
# Maintain two dictionaries:
# frequency {key: frequency} which helps to store the frequency of each key
# cache {frequency: OrderedDict} which stores all key value pairs with the same counter in a ordered dict

# Get Method:
# if not in the cache, return -1
# obtain the counter f of the key
# remove the key value pair from the ordered dict that corresponding to frequency f. If the ordered dict is empty, remove it from cache.
# If the frequency is equal to minimum frequency and the ordered dict is empty after removal, increment minimum frequency by 1
# insert the key value pair to the orderded dict that corresponding to frequency f+1
# update the frequency dict and return the value

# Set Method:
# call get method to check the presence and increment counter
# if key is not in the cache:
# if the cache is full, empty one spot
# update minimum frequency to 1, and put the key value pair to cache
# if key is in the cache, only need to update the value

# analysis
# time complexity is to be decided for each method. As suggested in the question, get and set have time complexity of
# T = O(n)

# the number of items in the dictionary will increase with the number of commands
# so if there are n commands, space complexity is
# S = O(n)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFrequency = 1
        self.cache = defaultdict(OrderedDict)   # dict {frequency : orderedDict({key, value})}
        self.frequency = {}                     # dict {key : frequency}

    def get(self, key: int) -> int:
        if key not in self.frequency:
            return -1
        f = self.frequency[key]     # get the counter
        self.frequency[key] = f + 1  # update the counter
        pairs = self.cache[f]
        res = pairs[key]
        del pairs[key]   # remove pair from ordered dict with frequency f
        if len(pairs) == 0:
            del self.cache[f]   # remove ordered dict if empty
            if f == self.minFrequency:
                self.minFrequency += 1  # update min frequency
        self.cache[f+1][key] = res   # put the pair to ordered dict with frequency f + 1

        return res

    def set(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        oldValue = self.get(key)
        if oldValue == -1: # key is not in the cache
            if len(self.frequency) == self.capacity and self.cache: # cache is full, empty one spot
                k, v = self.cache[self.minFrequency].popitem(last=False)
                del self.frequency[k]
                if len(self.cache[self.minFrequency]) == 0:
                    del self.cache[self.minFrequency]
            self.minFrequency = 1
            self.frequency[key] = 1
            self.cache[1][key] = value
        else: # key is in the cache, the frequency increment is done in get method
            self.cache[self.frequency[key]][key] = value    
