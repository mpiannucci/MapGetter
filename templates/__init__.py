from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>MapGetter</title>\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'    <link rel="stylesheet"    type="text/css"     href="/static/Styles/styles.css"  />\n'])
    extend_([u'    <script src="/static/Scripts/mapgetter.js" type="text/javascript"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div class="header" id="mainheader">\n'])
    extend_([u'        <h1>MapGetter</h1>\n'])
    extend_([u'        <em>Get static images of a central area with coorridinates in meters.</em>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="mapImage">\n'])
    extend_([u'        ', escape_(page, False), u'\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="footer" id="mainfooter">\n'])
    extend_([u'        <p>Copyright 2014, Matthew Iannucci</p>\n'])
    extend_([u'    </div>\n'])
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
    extend_([u'    <button id="mapbutton" type="button" onClick="handleGetMap();">Get My Map</button>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="mapimage" class="images">\n'])
    extend_([u'    <img src="" id="mapresult" />\n'])
    extend_([u'    <p id="urlprint">URL HERE</p>\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def map (url, opts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    if len(opts) > 5:
        opts[0] = opts[0].replace('+', ' ')
        extend_([u'<h2>Map of ', escape_(opts[0], True), u', ', escape_(opts[1], True), u', ', escape_(opts[2], True), u'</h2>\n'])
        extend_([u'<img src="', escape_(url, True), u'" />\n'])
    else:
        extend_([u'<h2>Map of ', escape_(opts[0], True), u',', escape_(opts[1], True), u'</h2>\n'])
        extend_([u'<img src="', escape_(url, True), u'" />\n'])

    return self

map = CompiledTemplate(map, 'templates/map.html')
join_ = map._join; escape_ = map._escape

