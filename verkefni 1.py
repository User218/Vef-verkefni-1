from bottle import route, run, template

#Alexander Örn

@route('/')
def index():
    return \
		"<a href='/about'>About </a><a href='/bio'>Bio </a><a href='/pic'>Pictures</a>"
	
@route('/about')
def about():
	return "Hér eru upplýsingar um Steve Jobs"

@route('/bio')
def bio():
	return "Hér er Biography frá Steve Jobs"

@route('/pic')
def pic():
	return "Hér er mynd af Steve Jobs"

run(host='localhost', port=8080)
