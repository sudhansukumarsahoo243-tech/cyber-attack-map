var map = L.map('map').setView([20,0],2);

L.tileLayer(
'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
).addTo(map);


fetch("/attacks")
.then(res => res.json())
.then(data => {

    console.log(data)

    data.data.slice(0,20).forEach(ip => {

        fetch("https://ipinfo.io/" + ip.ipAddress + "/json")
        .then(res => res.json())
        .then(loc => {

            if(!loc.loc) return;

            var coords = loc.loc.split(",")

            L.marker([coords[0],coords[1]])
            .addTo(map)
            .bindPopup("Attacker IP: " + ip.ipAddress)

        })

    })

    document.getElementById("count").innerText = data.data.length

})