from views import app
import os

app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 5000))
app.run(host='127.0.0.1', port=port)
