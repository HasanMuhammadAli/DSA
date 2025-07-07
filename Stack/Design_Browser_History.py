'''
Name: Muhammad Ali Mosin Hasan
Date: 7/7/25
Problem: 1472: Design Browser History
'''

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