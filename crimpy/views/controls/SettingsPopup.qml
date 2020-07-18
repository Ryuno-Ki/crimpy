import QtQuick 2.12
// Provides Popup
import QtQuick.Controls 2.12
// Provides StackLayout
import QtQuick.Layouts 1.15

Popup {
    x: 200
    y: 100
    height: 400
    width: 400
    modal: true
    focus: true

    ColumnLayout {
        TabBar {
            id: settings_bar
            width: parent.width

            TabButton {
                text: qsTr("Language")
            }
        }

        StackLayout {
            width: parent.width
            currentIndex: settings_bar.currentIndex

            Row {
                id: settings_language_tab
                Text {
                    text: "Choose a language"
                }
                Button {
                    text: "English"
                    onClicked: main.select_language("en")
                }
                Button {
                    text: "German"
                    onClicked: main.select_language("de")
                }
            }
        }
    }
}