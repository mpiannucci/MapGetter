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

// Return the size of the image in meters given the zoom and the size
// Uses equation found here: https://mail.google.com/mail/ca/u/0/#inbox/144dcfd00d6d569d
function scaleImage(size, lat, zoom) {
    var R_EARTH = 6378137;
    var ppm = (size) / ((Math.cos(lat*Math.PI/180) * 2*Math.PI * R_EARTH) / (256 * Math.pow(2, zoom))*600);
    return size/ppm;
}

// Handle the press of the main form button
function handleGetMap() {
    var cb = document.getElementById("coordcheck");
    var size = "&size=640x640";
    var scale = "&scale=2"; // Returns 1280x12080
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
        var meters = scaleImage(1280, lat, zoomval[zoomval.selectedIndex].value);
        var meterpix = document.getElementById("meterpixels");
        meterpix.innerHTML = meters + " Meters Wide , " + meters + " Meters Tall";
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
    var pic = document.getElementById("mapresult");
    pic.src = mapurl;
}