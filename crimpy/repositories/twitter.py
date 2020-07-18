import json
import os


class TwitterRepository(object):
    def __init__(self):
        super().__init__()
        self.rows = []

    def get_data(self):
        self.__fetch_data()
        # TODO: Add pagination
        return self.rows[:50]

    def __fetch_data(self):
        if len(self.rows) > 0:
            return

        takeout_path = os.path.abspath(
            os.path.join(
                os.path.abspath(__file__),
                "..",
                "..",
                "..",
                "resources",
                "tweet.json"
            )
        )
        with open(takeout_path, "r") as fh:
            content = fh.read()
        # Loaded upfront! Can really slow down intial load and responsiveness if loaded in full
        self.rows = json.loads(content)
