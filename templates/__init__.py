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
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/mobile.css" media="only screen and (max-device-width: 767px)" />\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/screen.css" media="only screen and (min-device-width: 768px)" />\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'    <div id="mapImage">\n'])
    extend_([u'        ', escape_(page, False), u'\n'])
    extend_([u'    </div>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

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

