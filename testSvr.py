import bottle

@bottle.route('/')
def root():
    return '''
    <html><body><center><h1>Hello world.</h1></center></body></html>
    '''

bottle.run(host='localhost', port=8888, debug=True)
