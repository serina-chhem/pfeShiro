from flask import Flask, render_template, request
import speech_recognition as sr 
app = Flask(__name__)

    
@app.route("/")



def record_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Parlez')
        audio = r.listen(source)
        voice_data = r.recognize_google(audio)
        print('Vous dites : ' + voice_data)
    
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)