'''
Name: Muhammad Ali Mosin Hasan
Date: 7/7/25
Problem: 1472: Design Browser History
'''

# using list and pointers
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current+1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history)-1, self.current + steps)
        return self.history[self.current]

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)

# using stacks

class BrowserHistory2:
    

    def __init__(self, homepage: str):
        self.current = []
        self.stk_b = []
        self.stk_f = []
        self.current.append(homepage)
        

    def visit(self, url: str) -> None:
        if self.current:
            self.stk_b.append(self.current[-1])
            self.current[-1] = url
        else:
            self.current.append(url)
        self.stk_f = []
    
    def back(self, steps: int) -> str:
        while steps > 0 and self.stk_b:
            self.stk_f.append(self.current[-1])
            self.current[-1] = self.stk_b.pop()
            steps -= 1
        return self.current[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.stk_f:
            self.stk_b.append(self.current[-1])
            self.current[-1] = self.stk_f.pop()
            steps -= 1
        return self.current[-1]
    
browserHistory = BrowserHistory2("leetcode.com")  # Start at homepage
browserHistory.visit("google.com")               # Visit google.com
browserHistory.visit("facebook.com")             # Visit facebook.com
print(browserHistory.back(1))                    # Back to google.com
print(browserHistory.back(1))                    # Back to leetcode.com
print(browserHistory.forward(1))                 # Forward to google.com
browserHistory.visit("youtube.com")              # Visit youtube.com (clears forward history)
print(browserHistory.back(2))                    # Back to leetcode.com
