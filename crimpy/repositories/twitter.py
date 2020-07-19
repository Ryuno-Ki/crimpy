from datetime import datetime
import json
import os

from pony import orm

from crimpy.models import TwitterModel


class TwitterRepository(object):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.__populate()

    @orm.db_session
    def get_data(self, page=0, page_size=10):
        begin_index = page * page_size
        end_index = (page + 1) * page_size
        tweets = TwitterModel.select()[begin_index:end_index]
        return [tweet for tweet in tweets]

    @orm.db_session
    def __populate(self):
        tweets = TwitterModel.select()
        if len(tweets) > 0:
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
        tweets_from_json = json.loads(content)

        new_tweets = []
        for tweet in tweets_from_json:
            t = TwitterModel(
                created_at=datetime.strptime(
                    tweet['tweet']['created_at'], "%a %b %d %H:%M:%S %z %Y"
                ),
                full_text=tweet['tweet']['full_text'],
                lang=tweet['tweet']['lang'],
                retweeted=tweet['tweet']['retweeted'],
                source=tweet['tweet']['source']
            )
            new_tweets.append(t)

        orm.commit()
