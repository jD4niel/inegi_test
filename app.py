from requests.api import request
from flask import Flask, render_template, request, redirect
from pprint import pprint
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def init():
    # Fetch data entity data from Inegi
    url = "https://gaia.inegi.org.mx/wscatgeo/mgee/"
    entity_request = requests.get(url).json()
    entity_data = entity_request.get('datos')
    entity_list = list(map(lambda x: (x['cve_agee'],x['nom_agee']),entity_data))
    # pass entity data to template
    data = {}
    token = '29cf1f94-1f44-4099-b6f1-195fe6f22c29'
    if request.method == 'POST':
        print("request.form: %s"%request.form)
        print("method called")
        entity = request.form.get('name')
        to = request.form.get('range')
        url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/restaurantes/{ entity }/1/{ to }/{ token }"

        data = requests.get(url).json()



    return render_template("index.html", entities=entity_list, data=data)

if __name__ == '__main__':
    app.run(debug=True)
