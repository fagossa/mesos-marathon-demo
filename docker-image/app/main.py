from bottle import route, run, template

@route('/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name

run(port=8080)
