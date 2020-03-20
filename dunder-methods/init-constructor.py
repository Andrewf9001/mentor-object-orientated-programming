class Invoice:

# a __init__ constructor function is automatically called when class is instantiated
    def __init__(self, client, total):
        # related directly to the instance self.client = google, when client set
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())