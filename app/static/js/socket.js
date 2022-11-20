let url = `ws://${window.location.host}/ws/socket-server/`

const scoket = new WebSocket(url)

scoket.onmessage = function(e){
    let data = JSON.parse(e.data)
    console.log('Data:', data)

    if (data.type === 'enter'){
        scoket.send(JSON.stringify({
            'message': 'connected'
        }))
    }
}
