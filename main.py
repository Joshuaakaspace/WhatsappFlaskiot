### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request
import pywhatkit as kit

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        x=str(request.form['science'])
        y=str(request.form['maths'])

        z=int(request.form['c'])
        j=int(request.form['datascience'])
        total_score= kit.sendwhatmsg(x, y, z,j)
        
    return "<html><body><h1>Sucess the message has been schuduled, </h1></body></html>"



if __name__ == '__main__' :
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--port", type=int, default=8080)
  args = parser.parse_agrs()
  start_server(predict, port=args.port)
  #app.run(debug=True)


    



    