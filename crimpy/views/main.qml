import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

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
	        text: qsTr(main.exit_label)
		onTriggered: Qt.quit()
	    }
	}
	Menu {
	    title: qsTr(main.help_menu_label)
	    MenuItem {
	        text: qsTr("&About")
		onTriggered: popup.open()
	    }
	}
    }
    
    Popup {
        id: popup
	x: 300
	y: 250
	height: 100
	width: 200
	modal: true
	focus: true
	closePolicy: Popup.CloseOnEscape

	contentItem: Text {
	    text: main.version
	}
    }

    TwitterModel {
        id: twitterModel
    }

    ListView {
        anchors.fill: parent
	model: twitterModel
	delegate: Item {
	    width: ListView.view.width
	    height: 30
	    Text {
	        text: display.tweet.full_text
	    }
	}

    }
}
