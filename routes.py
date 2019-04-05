from flask import Flask, render_template
from utils import FileOpener as Fo, CharacterEpisodeBundler as Cb,  TableBuilder as Tb
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():

    characters_obj        = Fo('characters.csv', 'rb')
    characters            = characters_obj.open_csv()

    appearances_obj       = Fo('episode_per_season.csv', 'rb')
    appearances           = appearances_obj.open_csv()

    character_episodes_obj = Cb(
        characters, appearances
        )
    character_episodes     = character_episodes_obj.bundle_characters_per_episodes()

    builder_object         = Tb(characters)
    page_data              = builder_object.build()

    return render_template('index.html', the_title='GOT Character Profiles', page_data = ''.join(page_data))



if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 8585, debug=True)
