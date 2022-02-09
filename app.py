from flask import Flask, jsonify, request # import statements

app = Flask(__name__) # creating an instance of Flask class

# json for our code
employees = {
    'e0001': {
        'name': 'ramkumar',
        'designation': 'project-manager',
        'business-unit': 'aws-bu',
        'work-location': 'chennai'
    },
    'e0002': {
        'name': 'rajkumar',
        'designation': 'team-lead',
        'business-unit': 'azure-bu',
        'work-location': 'mumbai'
    }
}

@app.route('/employees', methods=['GET'])
def home():
    return jsonify(employees)

@app.route('/employee/<string:empid>', methods=['GET'])
def getEmpById(empid):
    try:
        employees[empid]
        return jsonify(employees[empid])
    except:
        return jsonify({
            'Result': 'Employee ID not found',
            'Status Code': 404
        })

@app.route('/employee/add', methods=['POST'])
def addEmp():
    empid = 'e000'+str(len(employees)+1)
    employees[empid] = request.json
    return jsonify(200)

@app.route('/employee/edit/<string:empid>', methods=['PUT'])
def editEmp(empid):
    employees[empid].update(request.json)
    return jsonify({
        'Result': 'Data Updated',
        'Status Code': 200
        })

@app.route('/employee/delete/<string:empid>', methods=['DELETE'])
def deleteEmp(empid):
    employees.pop(empid)
    return {
        'Result': 'Data Deleted',
        'Status Code': 200
    }

@app.route('/', methods=['GET'])
def index():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug=True)