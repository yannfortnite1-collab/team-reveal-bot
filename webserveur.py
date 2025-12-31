from flask import Flask
fromt threading import thread



app = flask('')
@app.route('/')
def home():
    return "le bot est en ligne"


def run():
    app.run(host="0.0.0.0", port=8080)


    def keep_alive():
        t = thread(target=run)
        t.start()