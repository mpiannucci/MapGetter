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