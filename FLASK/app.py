from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello World!"
    return render_template('index.html')
    
@app.route('/dohyeon')
def dohyeon():
    return "저는 무술가 입니다."

@app.route('/html')
def html():
    return "<h1>태그도 사용할 수 있어요</h1>"

@app.route('/html_multiline')
def html_multiline():
    return '''
    <ol>
        <li>안녕</li>
        <li>안녕2</li>
    </ol>

    '''

# 동적 라우팅 (Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'안녕~, {name}??'
    return render_template('greeting.html', html_name=name)

# 세제곱을 돌려주는 cube 페이지 작성
# 사용자한테 숫자값을 받아, 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<string:num>')
def cube(num):
    a = int(num)
    b = a*a*a
    return render_template('cube.html', result=b)

@app.route('/cube2/<int:num>')
def cube2(num):
    return render_template('cube.html', result=num**3)

@app.route('/cube3/<int:num>')
def cube3(num):
    return render_template('cube3.html', number=num, result=num**3)

@app.route('/movies')
def movie():
    movie_list = ['82년생 김지영', '조커', '엔드게임', '궁예']
    return render_template('movies.html', movies=movie_list)

# ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다. 
@app.route('/ping')
def ping():
    return render_template('ping.html')

# pong : 사용자로부터 Form 데이터를 전달받아서 가공한다. 
# ping에서부터 데이터를 받음
# request 추가
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html', user_name=user_name)


# fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')

# fake google
@app.route('/google')
def google():
    return render_template('google.html')


# end of file !!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)