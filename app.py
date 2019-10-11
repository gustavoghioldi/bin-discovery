import pandas as pd
from flask import Flask, Response
import json
cc = pd.read_csv('data.csv', error_bad_lines=False)
app = Flask(__name__)

@app.route('/bin/<int:bin>')
def bin_recognition(bin):
    if not (len(str(bin))==6):
        return Response(json.dumps({"response":"el bin debe ser de 6 digitos"}), status=400, mimetype='application/json')
    query = 'bin=={}'.format(bin) 
    json_query = cc.query(query).to_dict('records')
    if len(json_query) != 1:
        return Response(json.dumps({"response":"no existe referencia para {}".format(bin)}), status=404, mimetype='application/json')
    return Response(json.dumps(json_query), status=200)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
