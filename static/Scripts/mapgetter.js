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

function handleGetMap(button) {
    var cb = document.getElementById("coordcheck");
    var size = "&size=640x640";
    var zoomval = document.getElementById("zoombox").value;
    var zoom = "&zoom=" + zoomval;
    var formt = "&format=png32";
    var mtype = "&maptype=satellite"
    var sensor = "&sensor=false"
    var StaticAPIKey = "&key=AIzaSyC96sP49qW-aePnuHnJnRZhGcSkvhIWNKs";
    var baseURL = "http://maps.googleapis.com/maps/api/staticmap?";

    if (cb.checked) {
        var lat  = document.getElementById("latbox").value;
        var lon  = document.getElementById("lonbox").value;
        var center = "center=" + lat + "," + lon;
    }
    else {
        var address = document.getElementById("addressbox").value;
        address.replace(" ", "+");
        var city    = document.getElementById("citybox").value;
        city.replace(" ", "+");
        var state   = document.getElementById("statebox").value;
        var center = "center=" + address + "," + city + "," + state;
    }
    url = baseURL + center + zoom + size + formt + mtype + sensor + StaticAPIKey;
    pic = document.getElementById("mapresult");
    pic.src = url;
}