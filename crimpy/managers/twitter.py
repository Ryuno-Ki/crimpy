from crimpy.repositories import TwitterRepository


class TwitterManager(object):
    def __init__(self):
        super().__init__()
        self.repository = TwitterRepository()

    def get_tweets(self):
        return self.repository.get_data()
