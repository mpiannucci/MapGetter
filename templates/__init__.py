from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n'])
    extend_([u'    <title>MapGetter</title>\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/styles.css" />\n'])
    extend_([u'    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n'])
    extend_([u'    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>\n'])
    extend_([u'    <script src="/static/Scripts/mapgetter.js" type="text/javascript"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
    extend_([u'<div  class="container">\n'])
    extend_([u'    <!-- Navigation Bar -->\n'])
    extend_([u'    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <!-- Brand and toggle get grouped for better mobile display -->\n'])
    extend_([u'            <div class="navbar-header">\n'])
    extend_([u'                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n'])
    extend_([u'                    <span class="sr-only">Toggle navigation</span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                </button>\n'])
    extend_([u'                <a class="navbar-brand" href="http://blog.mpiannucci.com/">Matthew Iannucci</a>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <!-- Collect the nav links, forms, and other content for toggling -->\n'])
    extend_([u'            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'])
    extend_([u'                <ul class="nav navbar-nav">\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="http://blog.mpiannucci.com/blog">Blog</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="http://blog.mpiannucci.com/apps">Projects</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="http://blog.mpiannucci.com/bio">About</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                </ul>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <!-- /.navbar-collapse -->\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- /.container -->\n'])
    extend_([u'    </nav>\n'])
    extend_([u'    <header class="jumbotron map_jumbotron" id="mainheader">\n'])
    extend_([u'        <h1>MapGetter</h1>\n'])
    extend_([u'        <em>Get static images of a central area with coorridinates in meters.</em>\n'])
    extend_([u'    </header>\n'])
    extend_([u'    <div id="mapImage">\n'])
    extend_([u'        ', escape_(page, False), u'\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="row">\n'])
    extend_([u'        <div class="col-lg-12 text-center" id="mainfooter">\n'])
    extend_([u'            <p>Copyright 2014, Matthew Iannucci</p>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def index (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="mapforms" class="forms">\n'])
    extend_([u'    <form name="mapform" >\n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'    </form>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="mapimage" class="images">\n'])
    extend_([u'    <img src="" id="mapresult" />\n'])
    extend_([u'    <h3 id="meterpixels"></h3>\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

