class Browser:
    def __init__(self, homepage: str):
        self.page = homepage
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Browser(homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        self.tail.next = Browser(url)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def back(self, steps: int) -> str:
        curr = self.tail
        while steps > 0 and curr.prev:
            steps -=1
            curr = curr.prev
        self.tail = curr
        return curr.page

        

    def forward(self, steps: int) -> str:
        curr = self.tail
        while steps > 0 and curr.next:
            steps -=1
            curr = curr.next
        self.tail = curr
        return curr.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)