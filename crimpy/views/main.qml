import QtQuick 2.12
// Provides MenuBar, Menu and MenuItem
import QtQuick.Controls 2.12
// Provides ApplicationWindow
import QtQuick.Window 2.12

import "controls" as Crimpy
import Twitter 1.0

ApplicationWindow {
    title: "Crimpy - Python CRM"
    width: 800
    height: 600
    visible: true

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
			MenuItem {
				text: qsTr("&Settings")
				onTriggered: settings.open()
			}
            MenuItem {
                text: qsTr("&Quit")
                onTriggered: Qt.quit()
            }
        }
        Menu {
            title: qsTr("&Help")
            MenuItem {
                text: qsTr("&About")
                onTriggered: popup.open()
            }
        }
    }

	Crimpy.VersionPopup {
		id: popup
	}

	Crimpy.SettingsPopup {
		id: settings
	}

    TwitterModel {
        id: twitterModel
    }

    Column {
        anchors.fill: parent
        Repeater {
            model: twitterModel
            delegate: Row {
                Text {
                    text: display.tweet.full_text
                }
            }
        }
	}
}
