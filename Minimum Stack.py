class MinimumStack:
    def __init__(self):
        self.data = []

    def append(self, val):
        if len(self.data) == 0:
            self.data.append((val, val))
            return
        curr_minimum = self.data[-1][1]
        if val < curr_minimum:
            self.data.append((val, val))

        else:
            self.data.append((val, curr_minimum))

    def peek(self):
        return self.data[-1][0]


    def min(self):
        return self.data[-1][1]


    def pop(self):
        return self.data.pop()[0]
        
