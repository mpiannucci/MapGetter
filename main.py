import web
import ConfigParser

# Map out the URLs
urls = (
    '/', 'Index',
    '/mapc(.+)', 'MapCenter', 
    '/mapl(.+)', 'MapLatLon'
)

# Set the debugging messages
web.config.debug = True

### Define the globals
t_globals = {
    'datestr': web.datestr,
}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web application
app = web.application(urls, globals())

config = ConfigParser.RawConfigParser()
config.read('key.cfg')
StaticAPIKey = config.get('api-keys', 'mapskey')

##------------------------------------------------------------------------
## Form Definitions

zoomvalues = []
for i in range(5, 20):
    tup = (str(i), str(i))
    zoomvalues.append(tup)

map_form = web.form.Form(web.form.Textbox('Address', id='addressbox'),
                              web.form.Textbox('City', id='citybox'),
                              web.form.Textbox('State', id='statebox'),
                              web.form.Textbox('Latitude', id='latbox'), 
                              web.form.Textbox('Longitude', id='lonbox'),
                              web.form.Dropdown('zoomdrop', zoomvalues, id='zoomdrop'),
                              web.form.Button('Get My Map', id='citybutton'))

##------------------------------------------------------------------------
## Web Page Class Definitions

class Index:
    '''Main index page'''
    def GET(self):
        form = map_form()
        return render.index(form)

class MapCenter:
    '''Show the static map image around a center'''
    def GET(self, options):
        # Options: 0=Address, 1=City, 2=State, 3=zoom, 4=typeofmap(satellite), 5=format(png32)
        # Options should be comma delimited
        opts = options.split(',')
        baseURL = 'http://maps.googleapis.com/maps/api/staticmap?'
        center = 'center=' + opts[0] + ',' + opts[1] + ',' + opts[2]
        center.replace(' ', '+')
        zoom = '&zoom=' + str(opts[3])
        mtype = '&maptype=' + opts[4]
        formt = '&format=' + opts[5]
        size = '&size=640x640'    # Biggest size for non paid accounts
        sensor = "&sensor=false"  # We will never us the users location
        apikey = '&key=' + StaticAPIKey
        url = baseURL + center + zoom + size + mtype + formt + sensor + apikey
        return render.map(url, opts)

class MapLatLon:
    '''Show the static map image around a lat,lon pair'''
    def GET(self, options):
        # Options: 0=lat, 1=lon, 2=zoom, 3=typeofmap(satellite), 4=format(png32)
        # Options should be comma delimited
        opts = options.split(',')
        baseURL = 'http://maps.googleapis.com/maps/api/staticmap?'
        center = 'center=' + str(opts[0]) +',' + str(opts[1])
        zoom = '&zoom=' + str(opts[2])
        mtype = '&maptype=' + str(opts[3])
        formt = '&format=' + str(opts[4])
        size = '&size=640x640'    # Biggest size for non paid accounts
        sensor = "&sensor=false"  # We will never us the users location
        apikey = '&key=' + StaticAPIKey
        url = baseURL + center + zoom + size + mtype + formt + sensor + apikey
        return render.map(url, opts)

def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

### Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()