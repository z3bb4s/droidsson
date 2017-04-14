#  this is the file that is invoked to start up a development server. It gets a copy of the app
# from your package and runs it. This wont be used in production, but it will see
# lot of mileage in development
from myapp import app

import myapp.views

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
