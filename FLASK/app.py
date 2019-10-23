from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
    # return render_template('index.html')
    
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


# end of file !!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)