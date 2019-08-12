from flask import Flask, Response
#import sse
import os
import time
#jsonify and json dumps

app = Flask(__name__)

# Can inject. All the routes declared here are prefixed with "/streams"
#app.register_blueprint( sse, url_prefix='/streams' )

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/whoami')
def who_am_i():
    # respond with an object of filetype (mimetype)
    return Response( "Christian Sewing", mimetype="text" )

@app.route('/time')
def what_is_the_time():
    def eventStream():
        while True:
            time.sleep(1)
            yield get_time() + '\n'
    # eventStream keeps stream open so data can keep going in
    return Response( eventStream(), mimetype="text/event-stream" )


def get_time():
    curr = time.ctime(time.time())
    return curr

def bootapp():
    app.run(debug=True, threaded=True, host=('0.0.0.0'))


if __name__ == '__main__':
     bootapp()