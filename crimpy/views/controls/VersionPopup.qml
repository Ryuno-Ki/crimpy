import QtQuick 2.12
// Provides Popup
import QtQuick.Controls 2.12

Popup {
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
