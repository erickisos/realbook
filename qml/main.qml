import QtQuick 2.0
import QtQuick.Controls 2.0

ApplicationWindow {
    visible: true
    title: "Realbook"
    width: 480
    height: 640
    color: "white"

    property string currentTime: "00: 00: 00"
    property QtObject timeBackend

    Connections {
        target: timeBackend
        function onTimeUpdated(time)
        {
            currentTime = time
        }
    }


    Text {
        anchors.centerIn: parent
        text: currentTime
        font.pixelSize: 48
    }
}
