#! /usr/bin/env python
from fbapp import app
app.config.from_object('config')

if __name__ == "__main__":
    app.run(debug=True)