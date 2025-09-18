
### `/src/history.py` (starter)

class _N:
    __slots__ = ("url", "prev", "next")
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        ...

    def visit(self, url):
        """If not at the end, drop all forward entries, then append url and move cursor."""
        ...

    def back(self, steps=1):
        ...

    def forward(self, steps=1):
        ...
    