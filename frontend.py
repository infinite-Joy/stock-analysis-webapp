
import os
from flask import Flask
app = Flask(__name__)

# run in background
import os
cmd = 'python background_task.py &'
pid = os.system(cmd)
print pid

@app.route("/")
def hello():
    with open("companies.txt", 'r') as f:
        page = f.readlines()
        return "".join(str(page))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
