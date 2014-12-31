import web

# Map out the URLs
urls = (
    '/', 'Index',
)

# Set the debugging messages
web.config.debug = True

# Define the globals
t_globals = {
}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web application
app = web.application(urls, globals())

# ------------------------------------------------------------------------
# Web Page Class Definitions

class Index:
    '''Main index page'''
    def GET(self):
        return render.index()

def notfound():
    ''' Create the not found page '''
    return web.notfound('Sorry, the page you were looking for was not found.')
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))

def internalerror():
    ''' Create the internal error page '''
    return web.internalerror('The server says: No soup for you!')

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()