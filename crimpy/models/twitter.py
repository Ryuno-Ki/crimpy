from PySide2.QtCore import QAbstractListModel, Qt

from crimpy.repositories import TwitterRepository


class TwitterModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.repository = TwitterRepository()

    def get_data(self):
        return self.repository.get_data()

    def data(self, index, role):
        rows = self.repository.get_data()
        
        if (role == Qt.DisplayRole and
            index.row() >= 0 and
            index.row() < len(rows)):
            return self.__get_value(index.row(), index.column())
        else:
            return None

    def rowCount(self, parent):
        rows = self.repository.get_data()

        return len(rows)

    def __get_value(self, row, column):
        rows = self.repository.get_data()

        return rows[row]

    def __update(self):
        rows = self.repository.get_data()
        
        self.dataChanged.emit(self.index(0, 0), self.index(rows[-1], 0))

