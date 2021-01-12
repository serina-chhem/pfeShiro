from flask import Flask, render_template
import speech_recognition as sr
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stt')
def stt():
    transcript = ""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Parlez')
        audio = r.listen(source)
        transcript = r.recognize_google(audio)
        print("Vous dites : " + transcript)
    return render_template("stt.html", transcript = transcript)

if __name__ == '__main__':
    app.run(debug = True, threaded = True)