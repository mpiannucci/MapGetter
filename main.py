import web

# Map out the URLs
urls = (
    '/', 'Index',
)

# Set the debugging messages
web.config.debug = True

### Define the globals
t_globals = {
}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web application
app = web.application(urls, globals())

##------------------------------------------------------------------------
## Form Definitions

zoomvalues = []
for i in range(5, 20):
    tup = (str(i), str(i))
    zoomvalues.append(tup)

map_form = web.form.Form(web.form.Checkbox('By Coordinates', checked=True, id="coordcheck", onClick='handleCheck(this);'),
                         web.form.Textbox('Address', id='addressbox', disabled=False),
                         web.form.Textbox('City', id='citybox', disabled=False),
                         web.form.Textbox('State', id='statebox', disabled=False),
                         web.form.Textbox('Latitude', id='latbox'),
                         web.form.Textbox('Longitude', id='lonbox'),
                         web.form.Dropdown('Zoom', zoomvalues, id='zoomdrop'),
                         web.form.Button('Get My Map', id='formbutton', type='button', onClick='handleGetMap()'))

##------------------------------------------------------------------------
## Web Page Class Definitions

class Index:
    '''Main index page'''
    def GET(self):
        form = map_form()
        return render.index(form)

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