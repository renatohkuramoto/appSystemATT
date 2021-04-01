from flask import Flask
from dashboard.views import dashboard
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'mDzjUywfkYtXRhLx0RrWSEG0XMQeENm5Nj5s0u40Gudkk7EuNiq0zaBIoUtU7hyiMuKyps8ZxerE41UqmaMnuxCGh9smEaSoiJiLr2TmmiLeaRqbiI6Jr2znAFTObTNj'
CORS(app, supports_credentials=True)

app.register_blueprint(dashboard)


if __name__ == '__main__':
    app.run()
