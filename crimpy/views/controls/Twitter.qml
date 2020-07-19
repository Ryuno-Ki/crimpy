import QtQuick 2.12

import Twitter 1.0

TableView {
    TwitterModel {
        id: twitterModel
    }

    id: tableView
    model: twitterModel
    anchors.fill: parent

    columnWidthProvider: function (column) { return 100; }
    rowHeightProvider: function (column) { return 60; }

    delegate: Rectangle {
        Text {
            text: display
            anchors.fill: parent
            anchors.margins: 10
        }
    }

    Row {
        id: columnsHeader
        y: tableView.contentY

        Repeater {
            model: tableView.columns
            Rectangle {
                Text {
                    text: twitterModel.headerData(modelData, Qt.Horizontal)
                    padding: 10
                    height: 35
                    width: tableView.columnWidthProvider(modelData)
                }
            }
        }
    }

    Column {
        id: rowsHeader
        x: tableView.contentX

        Repeater {
            model: tableView.rows
            Rectangle {
                Text {
                    text: twitterModel.headerData(modelData, Qt.Vertical)
                    padding: 10
                    height: tableView.rowHeightProvider(modelData)
                    width: 60
                }
            }
        }
    }
}