from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('complex1')
parser.add_argument('complex2')
def Add(complex1,complex2):
    complex1 = str(complex1).replace('i','j')
    complex2 = str(complex2).replace('i','j')
    complex1 = complex(complex1)
    complex2 = complex(complex2)
    complexR = str(complex1+complex2)
    complexR = complexR.replace('(','').replace(')','').replace('j','i')
    return complexR
def Sub(complex1,complex2):
    complex1 = str(complex1).replace('i','j')
    complex2 = str(complex2).replace('i','j')
    complex1 = complex(complex1)
    complex2 = complex(complex2)
    complexR = str(complex1-complex2)
    complexR = complexR.replace('(','').replace(')','').replace('j','i')
    return complexR
def Multiply(complex1,complex2):
    complex1 = str(complex1).replace('i','j')
    complex2 = str(complex2).replace('i','j')
    complex1 = complex(complex1)
    complex2 = complex(complex2)
    complexR = str(complex1*complex2)
    complexR = complexR.replace('(','').replace(')','').replace('j','i')
    return complexR
class ApiAdd(Resource):
	def post(self):
		args = parser.parse_args()
		complex1 = json.loads(args['complex1'])
		complex2 = json.loads(args['complex2'])
		return {'complex ':Add(complex1,complex2)}

class ApiSub(Resource):
	def post(self):
		args = parser.parse_args()
		complex1 = json.loads(args['complex1'])
		complex2 = json.loads(args['complex2'])
		return {'complex ':Sub(complex1,complex2)}
class ApiMultiply(Resource):
	def post(self):
		args = parser.parse_args()
		complex1 = json.loads(args['complex1'])
		complex2 = json.loads(args['complex2'])
		return {'complex ':Multiply(complex1,complex2)}
api.add_resource(ApiAdd,'/Add')
api.add_resource(ApiSub,'/Sub')
api.add_resource(ApiMultiply,'/Multiply')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)

