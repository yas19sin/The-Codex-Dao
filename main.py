"""
Create a Flask website that has multiple generator sections each section has one "Generate" button and Output zone
1. Import generate_character() from main_character, Import generate_plane_name() from plane_names, Import generate_random_cultivation_realm() from cultivation_realms, Import generate_cultivation_technique() from cultivation_techniques, Import generate_sect_name() from cultivation_sects, Import generate_random_name() from daoist_titles_names, Import generate_face_slap() from face_slapping, Import generate_forbidden_name() from forbidden_areas_names, Import generate_restaurant_chapter() from chapter_slapping_at_restaurant, Import generate_physique_name() from physique_names, Import generate_pill_name() from pill_names, Import generate_planet_name() from planet_names, Import generate_special_technique() from special_techniques, Import generate_herb_name() from spirit_herbs
1. Website page should have a "Welcome to Generate you Xianxia/Xuanhuan World" center in a header
2. Below the header should be a description with a sentence that says "Create you own novel world, main character, sect names and more"
3. Write the rest of needed code
"""

from flask import Flask, render_template, request
from main_character import generate_character
from plane_name import generate_plane_name
from cultivation_realms import generate_random_cultivation_realm
from cultivation_techniques import generate_cultivation_technique
from cultivation_sects import generate_sect_name
from daoist_titles_names import generate_random_name
from face_slapping import generate_face_slap
from forbidden_areas_names import generate_forbidden_name
from chapter_slapping_at_restaurant import generate_restaurant_chapter
from physique_names import generate_physique_name
from pill_names import generate_pill_name
from planet_names import generate_planet_name
from special_techniques import generate_special_technique
from spirit_herbs import generate_herb_name
from beats_names import generate_beast_name
from formation_arrays import generate_random_formation_array

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html", generate_character=generate_character(),
                               generate_plane_name=generate_plane_name(),
                               generate_random_cultivation_realm=generate_random_cultivation_realm(),
                               generate_cultivation_technique=generate_cultivation_technique(),
                               generate_random_formation_array=generate_random_formation_array(),
                               generate_sect_name=generate_sect_name(),
                               generate_random_name=generate_random_name(), generate_face_slap=generate_face_slap(),
                               generate_forbidden_name=generate_forbidden_name(),
                               generate_restaurant_chapter=generate_restaurant_chapter(),
                               generate_physique_name=generate_physique_name(), generate_pill_name=generate_pill_name(),
                               generate_planet_name=generate_planet_name(),
                               generate_special_technique=generate_special_technique(),
                               generate_herb_name=generate_herb_name(), generate_beast_name=generate_beast_name())
    if request.method == 'POST':
        # check if

        if request.form['submit'] == 'Generate Character':
            return render_template("index.html", generate_character=generate_character())
        elif request.form['submit'] == 'Generate Plane Name':
            return render_template("index.html", generate_plane_name=generate_plane_name())
        elif request.form['submit'] == 'Generate Cultivation Realm':
            return render_template("index.html", generate_random_cultivation_realm=generate_random_cultivation_realm())
        elif request.form['submit'] == 'Generate Cultivation Technique':
            return render_template("index.html", generate_cultivation_technique=generate_cultivation_technique())
        elif request.form['submit'] == 'Generate Formation Array':
            return render_template("index.html", generate_random_formation_array=generate_random_formation_array())
        elif request.form['submit'] == 'Generate Sect Name':
            return render_template("index.html", generate_sect_name=generate_sect_name())
        elif request.form['submit'] == 'Generate Daoist Name':
            return render_template("index.html", generate_random_name=generate_random_name())
        elif request.form['submit'] == 'Generate Face Slap':
            return render_template("index.html", generate_face_slap=generate_face_slap())
        elif request.form['submit'] == 'Generate Forbidden Name':
            return render_template("index.html", generate_forbidden_name=generate_forbidden_name())
        elif request.form['submit'] == 'Generate Restaurant Chapter':
            return render_template("index.html", generate_restaurant_chapter=generate_restaurant_chapter())
        elif request.form['submit'] == 'Generate Physique Name':
            return render_template("index.html", generate_physique_name=generate_physique_name())
        elif request.form['submit'] == 'Generate Pill Name':
            return render_template("index.html", generate_pill_name=generate_pill_name())
        elif request.form['submit'] == 'Generate Planet Name':
            return render_template("index.html", generate_planet_name=generate_planet_name())
        elif request.form['submit'] == 'Generate Special Technique':
            return render_template("index.html", generate_special_technique=generate_special_technique())
        elif request.form['submit'] == 'Generate Spirit Herb':
            return render_template("index.html", generate_herb_name=generate_herb_name())
        elif request.form['submit'] == 'Generate Beast Name':
            return render_template("index.html", generate_beast_name=generate_beast_name())
        else:
            return render_template("index.html")


if __name__ == "__main__":
    app.run()