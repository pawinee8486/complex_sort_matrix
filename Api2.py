from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('listnum')
def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] > A[k - 1] ):
        swap( A, k, k - 1 )
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] > pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part



def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] > righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1



class ApiBubble(Resource):
	def post(self):
		args = parser.parse_args()
		listnum = json.loads(args['listnum'])
                listnum = map(int,listnum.split(','))
		Bubble(listnum)
		return {'listnum':listnum}

class ApiQuick(Resource):
	def post(self):
		args = parser.parse_args()
		listnum = json.loads(args['listnum'])
                listnum = map(int,listnum.split(','))
		Quick(listnum)
		return {'listnum':listnum}
class ApiMerge(Resource):
	def post(self):
		args = parser.parse_args()
		listnum = json.loads(args['listnum'])
                listnum = map(int,listnum.split(','))
		Merge(listnum)
		return {'listnum':listnum}
api.add_resource(ApiBubble,'/Bubble')
api.add_resource(ApiQuick,'/Quick')
api.add_resource(ApiMerge,'/Merge')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)

