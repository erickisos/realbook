import QtQuick 2.0
import QtQuick.Controls 2.0

ApplicationWindow {
    visible: true
    title: "Realbook"
    width: 480
    height: 640
    color: "white"

    property string currentTempo: "90"
    property QtObject metronomeBackend

    Text {
        text: currentTempo

        Connections {
            target: metronomeBackend

            function onTempoUpdated(tempo)
            {
                currentTempo = tempo
            }
        }
    }

    Button {
        text: "Tap"
        onClicked: metronomeBackend.tempoTapped()
    }
}
