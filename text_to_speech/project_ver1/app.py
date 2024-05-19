from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
from langdetect import detect

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/generate', methods=['GET','POST'])
def generate():
    audio_file = None
    if request.method == 'POST':
        data = request.form['data']

        lang  = detect(data)   #detect the language of data

        # text to speech logic 
        if data:
            sound = gTTS(text=data, lang=lang)
            file_path = 'static/generated_audios/audio.mp3'
            sound.save(file_path)

    return render_template('generate.html', audio_file='generated_audios/audio.mp3' , lang=lang)


if __name__=='__main__':
    app.run(debug=True)