class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    # use when you want to have a nice and clean output
    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'

    # use when working with Raw data
    def __repr__(self):
        return f'Invoice <value: client: {self.client}, total: {self.total}>'


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))