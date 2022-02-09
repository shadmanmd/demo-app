from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

@app.route('/ui/employees')
def home():
    return render_template('index.html', employees=employees)

@app.route('/ui/employee/edit/<string:empid>', methods=['GET', 'POST'])
def editEmployee(empid):
    if request.method=='GET':
        employee = employees[empid]
        return render_template('editemp.html', employee=employee, empid=empid)
    empid = request.form['empid']
    name = request.form['name']
    work_location = request.form['work-location']
    business_unit = request.form['business-unit']
    designation = request.form['designation']
    employees[empid] = {
        'name': name,
        'designation': designation,
        'work-location': work_location,
        'business-unit': business_unit
    }
    return redirect(url_for('home'))

@app.route('/ui/employee/add', methods=['GET','POST'])
def addEmployee():
    if request.method=='GET':
        empid = 'e000'+str(len(employees)+1)
        return render_template('addemp.html', empid=empid)
    empid = request.form['empid']
    name = request.form['name']
    work_location = request.form['work-location']
    business_unit = request.form['business-unit']
    designation = request.form['designation']
    employees[empid] = {
        'name': name,
        'designation': designation,
        'work-location': work_location,
        'business-unit': business_unit
    }
    return redirect(url_for('home'))

@app.route('/ui/employee/delete/<string:empid>', methods=['GET'])
def deleteEmployee(empid):
    employees.pop(empid)
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)