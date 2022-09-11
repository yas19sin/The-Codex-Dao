import datetime
import threading
import time
import traceback
import os

from flask import Flask, render_template, request, url_for
import pywhatkit
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import database as db

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dofusilyas'

db.init_app(app)

config = ConfigParser()
config.read('config.ini')

# https://vente.tryandjudge.com/dofuskamas.php | Jahash
url = 'https://vente.tryandjudge.com/dofuskamas.php'
message = ''
check_interval = 0
server_List = []
whatsapp_number = ''  # '+212675754657' ilyas' whatsapp # '+212709701487' <- my inwi whatsapp

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-sh-usage")
chrome_options.add_argument("-no-gpu")
# chrome_options.add_argument('window-size=1920x1080')


def every(delay, task):
    next_time = time.time() + delay
    while True:
        time.sleep(max(0, next_time - time.time()))
        # noinspection PyBroadException
        try:
            task()
        except Exception:
            traceback.print_exc()
            break
            # in production code you might want to have this instead of course:
            # logger.exception("Problem while executing repetitive task.")
        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) // delay * delay + delay


def check_server():
    search_for_server_state(server_name='')


def get_sending_time():
    today = datetime.datetime.now()
    date_time = today.strftime("%H:%M")
    h = int(date_time.split(':')[0])
    m = int(date_time.split(':')[1])
    return h, m


def search_for_server_state(server_name):
    found = False
    tries = 3
    server_found = ''
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url)
    server_price_list = driver.find_element(By.ID, 'contentprices')
    rows = server_price_list.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        if tries <= 0:
            hour, minute = get_sending_time()
            if 'Cliquez' in server_found:
                pywhatkit.sendwhatmsg_instantly(whatsapp_number, server_name + message, 5, True, 20)
                print(f'Whatsapp message sent at {hour}:{minute}, {server_name + message}')
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
            break

        if found is True:
            tries -= 1

        if server_name in row.text:
            server_found = row.text
            tries -= 1
            found = True
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')


def get_servers():
    server_found = []
    skip = 0
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url)
    server_price_list = driver.find_element(By.ID, 'contentprices')
    rows = server_price_list.find_elements(By.TAG_NAME, 'td')
    for row in rows:
        if skip == 0:
            server_found.append(row.text)
            skip = 2
        else:
            skip -= 1

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
    driver.close()
    driver.quit()
    return server_found


def get_server(sr_name):
    server_found = {}
    i = 0
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url)
    server_price_list = driver.find_element(By.ID, 'contentprices')
    rows = server_price_list.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        if sr_name in row.text:
            split = row.find_elements(By.TAG_NAME, 'td')
            for splits in split:
                server_found[i] = splits.text
                i += 1

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
    driver.close()
    driver.quit()
    return server_found[0], server_found[1], server_found[2]


def runConfig():
    config.add_section('Ilyas Configuration')
    config.set('Ilyas Configuration', 'Whatsapp_Number', '+212675754657')
    config.set('Ilyas Configuration', 'Message', ' Server est disponible en option de vente')
    config.set('Ilyas Configuration', 'Interval', '60')

    with open('config.ini', 'w') as f:
        config.write(f)


def readConfig():
    global whatsapp_number, message, check_interval
    whatsapp_number = config.get('Ilyas Configuration', 'Whatsapp_Number')
    message = config.get('Ilyas Configuration', 'Message')
    check_interval = config.getint('Ilyas Configuration', 'Interval')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sname = request.values.get('servers')
        print('Post Method')
        print(sname)
        server_name, price, state = get_server(sname)
        if not db.get_serverinfo(sname):
            db.set_serverinfo(server_name, price, state)
            return render_template('check.html', check=db.get_serverinfo(sname)), {"Refresh": "5, url=/"}
        else:
            return render_template('check.html', check=db.get_serverinfo(sname)), {"Refresh": "5, url=/"}
    elif request.method == 'GET':
        dbservers = db.Servers.query.all()
        return render_template('home.html', servers=server_List, dbservers=dbservers)
    return render_template('home.html')


@app.route('/check')
def check():
    return render_template('check.html'), {"Refresh": "5; url=/"}


@app.route('/add')
def add():
    name = request.args.get('name', default='*', type=str)
    return render_template('add.html', name=name), {"Refresh": "5; url=/"}


@app.route('/remove')
def remove():
    name = request.args.get('name', default='*', type=str)
    db.deleteAll()
    return render_template('remove.html', name=name), {"Refresh": "5; url=/"}


if __name__ == '__main__':
    if config.has_section('Ilyas Configuration') is False:
        runConfig()
    readConfig()
    server_List = get_servers()
    # threading.Thread(target=lambda: every(check_interval, check_server)).start()
    app.run()
