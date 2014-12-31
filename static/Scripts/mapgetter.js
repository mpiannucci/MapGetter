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
        }
        for (var j=0; j<llTextIds.length; j++) {
            llTextIds[j].disabled = false;
        }
    }
    else {
        for (var k=0; k<cityTextIds.length; k++) {
            cityTextIds[k].disabled = false;
        }
        for (var l=0; l<llTextIds.length; l++) {
            llTextIds[l].disabled = true;
        }
    }
}

// Return the size of the image in meters given the zoom and the size
// Uses equation found here: https://mail.google.com/mail/ca/u/0/#inbox/144dcfd00d6d569d
function scaleImage(size, lat, zoom) {
    var R_EARTH = 6378137;
    var ppm = (size) / ((Math.cos(lat*Math.PI/180) * 2*Math.PI * R_EARTH * 640) / (256 * Math.pow(2, zoom)));
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
    var mtype = "&maptype=satellite";
    var sensor = "&sensor=false";
    var StaticAPIKey = "&key=AIzaSyC96sP49qW-aePnuHnJnRZhGcSkvhIWNKs";
    var baseURL = "http://maps.googleapis.com/maps/api/staticmap?";
    var lat, lon, state, city, address, center;
    if (cb.checked) {
        lat = document.getElementById("latbox").value;
        lon = document.getElementById("lonbox").value;
        center = "center=" + lat + "," + lon;
        var meters = scaleImage(1280, lat, zoomval[zoomval.selectedIndex].value);
        document.getElementById("resultbox").disabled = false;
        document.getElementById("resultbox").value = meters;
        document.getElementById("resultbox").focus();
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