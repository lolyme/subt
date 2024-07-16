import os
import moviepy.editor as mp
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
data= request.POST.get('data','')
data= request.POST
clip = mp.VideoFileClip("C:\\Users\\lesko\\Videos\\Google.mp4").subclip(0,20)
clip.audio.write_audiofile("C:\\Users\\lesko\\Videos\\fltheaudio.mp3")

#data=  request.POST()
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
def my_function(nm):
  print("Hello from a function")
 
if __name__ == '__main__':
   app.run()
