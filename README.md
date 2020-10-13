# Photo Gallery

## Description
A django photo gallery app that give photographers a portfolio to showcase their images to potential clients.

### Author
[Lennox Omondi](https://linkedin.com/in/lenomosh)
## Technologies used
- MDBootstrap
- FancyBox
- Typed.js
- Select2
- AOS
- Django
- Jquery

## User Stories
As a user of the application I should be able to:

   - View different photos that interest me.
   - Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
   - Search for different categories of photos. (ie. Travel, Food)
   - Copy a link to the photo to share with my friends.
   = View photos based on the location they were taken.



## Setup Instructions
- `git init` and run `git remote add origin git@github.com:lenomosh/photo-gallery.git` id you are using SSH or `https://github.com/lenomosh/photo-gallery.git`
-  From the project directory run `conda create --prefix=./env` or `python -m venv virtual`
- Run `source activate ./env` for conda or `source virtual/bin/activate`
- run`touch .env` in the root project directory and add the following to your file
```
SECRET_KEY='qqgv=a%hdsemzie05ro=2-6=vxb92%lr&6_c56lovs1p#p3k4cn8v'
DEBUG=True
DB_NAME='<your database_name>'
DB_USER='<your database username>'
DB_PASSWORD='<your database password>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS=.localhost, .herokuapp.com, .127.0.0.1
DISABLE_COLLECTSTATIC=1
CORS_ALLOWED_ORIGINS = http://localhost:8000, https://app-galla.herokuapp.com, http://127.0.0.1:8000
CSRF_TRUSTED_ORIGINS = http://localhost:8000, https://app-galla.herokuapp.com
```
- Run `pip install -r requirements.txt`
- Run `python manage.py migrate`
- Run `python manage.py createsuperuser` and follow the steps provided
- Your app your be able to start by running `python manage.py runserver`

## LICENSE
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Copyright (c) 2020 Lennox Omondi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.