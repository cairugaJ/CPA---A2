import pandas as pd
from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

#Lê arquivo JSON
INSTITUICOES_ENSINO = pd.read_json("DadosIES_Sul.json")

#PARSER
parser = reqparse.RequestParser()
parser.add_argument('SG_UF_IES')
parser.add_argument('TP_ORGANIZACAO_ACADEMICA', type = int)
parser.add_argument('TP_CATEGORIA_ADMINISTRATIVA', type = int)
parser.add_argument('NO_IES')
parser.add_argument('SG_IES')
parser.add_argument('NU_CEP_IES', type = float)
parser.add_argument('QT_DOC_TOTAL', type = int)
parser.add_argument('QT_DOC_EX_FEMI', type = int)
parser.add_argument('QT_DOC_EX_MASC', type = int)





if __name__ == '__main__':
    app.run(debug=True)