# GOT Character Profiles

**Routes** and **static files** are handled correctly in all `src` and `href` attributes in the template files.

The template file `base.html` is used as a shell by the other one HTML templates. This means they insert content into `base.html` according to Jinja2 template rules.

Create virtualenv and install requirements.txt 

`$ pip install -r requirements.txt`

Run Tests With nose2

`$ nose2`

Or 

`$ python -m unittest tests`


After installing all dependencies, run the app by entering its folder and typing:

`$ python routes.py`
