"""
Turn Twitter Model instances into a structure for QML.
"""
from PySide2.QtCore import QAbstractTableModel, Qt

from crimpy.managers import TwitterManager


class TwitterConnector(QAbstractTableModel):
    """
    Connects TwitterManager to QML via QAbstractTableModel
    """
    def __init__(self):
        super().__init__()
        self.__get_tweets()

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            # Table header
            return ("Text", "Retweeted")[section]
        else:
            # Table data
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):        
        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            if col == 0:
                tweet = self.tweets[row]
                return tweet.full_text
            elif col == 1:
                tweet = self.tweets[row]
                return str(tweet.retweeted)
        else:
            return None

    def columnCount(self, *args):
        return self.column_count

    def rowCount(self, *args):
        return self.row_count
    
    def __get_tweets(self):
        if not hasattr(self, 'manager'):
            self.manager = TwitterManager()
        self.tweets = self.manager.get_tweets()
        self.column_count = 2
        self.row_count = len(self.tweets)
