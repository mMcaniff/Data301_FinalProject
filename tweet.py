class Tweet:

    def __init__(self, tweet_json):
        self.id = tweet_json.id
        self.text = tweet_json.text
        self.user = tweet_json.user.name
        self.timestamp = tweet_json.created_at

    def __str__(self):
        return str(self.id) + "\t" + self.user + "\t" + str(self.timestamp) + "\t" + self.text + "\n"



