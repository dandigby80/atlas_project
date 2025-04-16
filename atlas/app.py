from flask import Flask, render_template
import psutil # To fetch system stats

app = Flask(__name__)

@app.route('/')
def index():
    # Get system stats
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return render_template('index.html', cpu=cpu, memory=memory)

if __name__ == '__main__':
    app.run(debug=True)