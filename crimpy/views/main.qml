import QtQuick 2.12
// Provides MenuBar, Menu and MenuItem
import QtQuick.Controls 2.12
// Provides ApplicationWindow
import QtQuick.Window 2.12

import "controls" as Crimpy

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

    Crimpy.Twitter {}
}
