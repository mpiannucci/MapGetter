MapGetter
=========

Gets a static map of a given location and displays the displays the size of the map in meters. This was originally made for the URI Autonomous Surface Vehicle Team to create map overlays to visualize simulations, and real-time GPS data. Knowing the size of the map image in meters allows accurate (decently) real time visualization of data received from synced GPS, compass, and accelerometers. 

Live at http://mapgetter.mpiannucci.com

#### Get the dependencies
```bash
cd MapGetter/
pip install web.py -t .
rm -rf web.*
```

#### Run the App
```bash
./Compiletemplates
dev_appserver.py .
```
