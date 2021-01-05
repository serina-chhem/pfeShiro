@app.route("/")

def record_audio():
    transcript = ""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Parlez')
        audio = r.listen(source)
        transcript = r.recognize_google(audio)
        print('Vous dites : ' + transcript)
    
    
    return render_template('index.html', transcript = transcript)


if __name__ == "__main__":