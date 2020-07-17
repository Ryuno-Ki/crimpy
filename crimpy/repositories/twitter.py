class TwitterRepository(object):
    def __init__(self):
        super().__init__()
        self.rows = []

    def get_data(self):
        self.__fetch_data()
        return self.rows

    def __fetch_data(self):
        self.rows = [{
            "tweet": {
                "full_text": "@ZUMTeam Naja"
            }
        }, {
            "tweet": {
                "full_text": "How exclusive."
            }
        }]
