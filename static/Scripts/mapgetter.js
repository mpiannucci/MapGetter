/************************************************************
 mapgetter.js -- MapGetter JavaScript definitions
 ***********************************************************/

// Handle the change in textbox state
function handleCheck(cb) {
    var cityTextIds = [document.getElementById("addressbox"),
                       document.getElementById("citybox"),
                       document.getElementById("statebox")];
    var llTextIds =   [document.getElementById("latbox"),
                       document.getElementById("lonbox")];
    if (cb.checked) {
        for (var i=0; i<cityTextIds.length; i++) {
            cityTextIds[i].disabled = true;
        };
        for (var i=0; i<llTextIds.length; i++) {
            llTextIds[i].disabled = false;
        };
    }
    else {
        for (var i=0; i<cityTextIds.length; i++) {
            cityTextIds[i].disabled = false;
        };
        for (var i=0; i<llTextIds.length; i++) {
            llTextIds[i].disabled = true;
        };
    }
}

function handleGetMap() {
    var cb = document.getElementById("coordcheck");
    var size = "&size=640x640";
    var scale = "&scale=2";
    var zoomval = document.getElementById("zoomdrop");
    var zoom = "&zoom=" + zoomval[zoomval.selectedIndex].value;
    var formt = "&format=png32";
    var mtype = "&maptype=satellite"
    var sensor = "&sensor=false"
    var StaticAPIKey = "&key=AIzaSyC96sP49qW-aePnuHnJnRZhGcSkvhIWNKs";
    var baseURL = "http://maps.googleapis.com/maps/api/staticmap?";
    var lat, lon, state, city, address, center
    if (cb.checked) {
        lat = document.getElementById("latbox").value;
        lon = document.getElementById("lonbox").value;
        center = "center=" + lat + "," + lon;
    }
    else {
        address = document.getElementById("addressbox").value;
        address.replace(" ", "+");
        city = document.getElementById("citybox").value;
        city.replace(" ", "+");
        state = document.getElementById("statebox").value;
        center = "center=" + address + "," + city + "," + state;
    }
    mapurl = baseURL + center + zoom + size + scale + formt + mtype + sensor + StaticAPIKey;
    var texter = document.getElementById("urlprint");
    texter.innerHTML = mapurl;
    var pic = document.getElementById("mapresult");
    pic.src = mapurl;
}