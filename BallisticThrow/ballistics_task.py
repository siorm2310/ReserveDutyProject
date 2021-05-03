import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    R,t,h = 0,0,0
    if request.method == 'POST':
        v=request.form['v']
        a=request.form['a']
        try:
            v = float(v)
            a = float(a)
            g = 10 #9.80665

            a = a*math.pi/180

            R = v*v*math.sin(2*a)/g
            t = 2*v*math.sin(a)/g
            h = (v*math.sin(a))**2/2/g
            R = f"{R:.3f}"
            t = f"{t:.3f}"
            h = f"{h:.3f}"

            mode = "show"
        except ValueError as err:
            if v == "" or a == "":
                mode = "empty"
            else:
                mode = "error"
    else:
        mode = "start"
    return render_template('ballistics_task.html', mode=mode, R=R, t=t, h=h, data={"R":R,"h":h})

if __name__ == '__main__':
    app.run(debug=True)
