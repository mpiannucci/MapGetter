/************************************************************
 mapgetter.js -- MapGetter JavaScript definitions
 ***********************************************************/

var lat_lon = [];

// Handle the change in textbox state
function handleCheck(cb) {
    var cityTextIds = [document.getElementById("addressbox"),
                       document.getElementById("citybox"),
                       document.getElementById("statebox")];
    var llTextIds =   [document.getElementById("latbox"),
                       document.getElementById("lonbox")];
    for (var i = 0; i < cityTextIds.length; i++) {
        cityTextIds[i].disabled = cb.checked;
    }
    for (var j = 0; j < llTextIds.length; j++) {
        llTextIds[j].disabled = !cb.checked;
    }
}

// Return the size of the image in meters given the zoom and the size
// Uses equation found here: https://mail.google.com/mail/ca/u/0/#inbox/144dcfd00d6d569d
function scaleImage(size, lat, zoom) {
    var R_EARTH = 6378137;
    var ppm = (size) / ((Math.cos(lat*Math.PI/180) * 2*Math.PI * R_EARTH * 640) / (256 * Math.pow(2, zoom)));
    return size/ppm;
}

// Updates the value of the of the result box 
function updateResultBox(latitude) {
    var zoomval = document.getElementById("zoomdrop");
    var meters = scaleImage(1280, latitude, zoomval[zoomval.selectedIndex].value);
    document.getElementById("resultbox").disabled = false;
    document.getElementById("resultbox").value = meters;
    document.getElementById("resultbox").focus();
}

// Get the latitude and logitude from the user given address
function getLatLong(address) {
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode( { 'address': address, 'region': 'us' }, function(results, status) {
        var result = []
        if (status == google.maps.GeocoderStatus.OK) {
            // Weee we have the location
            lat_lon= [results[0].geometry.location.lat(), results[0].geometry.location.lng()];
        } else {
            lat_lon = [0];
        }
        if (lat_lon[0] != 0) {
            updateResultBox(lat_lon[0]);
        }
    });
}

// Handle the press of the main form button
function handleGetMap() {
    // Configure the static map api data
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
        // Grab the lat and lon values from the form
        lat = document.getElementById("latbox").value;
        lon = document.getElementById("lonbox").value;

        // Where the map is centered
        center = "center=" + lat + "," + lon;

        // Get the resultant map size to show the user
        updateResultBox(lat);
    }
    else {
        // The Geo Address is the address string to send to the GeoCoding API
        geo_address = "";

        // Street Address
        address = document.getElementById("addressbox").value;
        geo_address = address;
        address.replace(" ", "+");

        // City
        city = document.getElementById("citybox").value;
        geo_address = geo_address + ", " + city;
        city.replace(" ", "+");

        // State
        state = document.getElementById("statebox").value;
        geo_address = geo_address + ", " + state;

        // Where the map is centered
        center = "center=" + address + "," + city + "," + state;
        
        // Get the latitude and longitude from Google Geocoding API
        getLatLong(geo_address);
    }
    // Show the map!!
    mapurl = baseURL + center + zoom + size + scale + formt + mtype + sensor + StaticAPIKey;
    var pic = document.getElementById("mapresult");
    pic.src = mapurl;
}

// Show the user a prompt to copy the size to the clipboard
function onSideLengthClick() {
    var side_length = document.getElementById("resultbox").value;
    window.prompt("Copy to clipboard: Ctrl+C, Enter", side_length);
}