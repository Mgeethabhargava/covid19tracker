from flask import Flask,session,flash,render_template,redirect,session,url_for,request,send_from_directory,send_file
from clist import cname,sname
from covid import Covid
import pydantic
import requests
from covid_india import states

app = Flask(__name__)
app.secret_key = 'Alexas'
 

@app.route('/')
def main():
    return render_template('covid.html')

@app.route('/covid19',methods = ['POST','GET'])
def covid19():
    return render_template('covid.html')

@app.route("/covidworld",methods = ['POST','GET'])
def covidworld():
    cnames = cname()
    covid =Covid()
    country = "World"    
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()
    data = {'confirmed':confirmed,'recovered':recovered,'deaths':deaths}
    return render_template('covidworld.html',data=data,country=country,cnames = cnames)
    #return render_template('covidworld.html',rows = rows)

@app.route("/country",methods = ['POST','GET'])
def covidcountry():
    if request.method == 'POST':
        cnames = cname()
        covid = Covid()
        #covid = covid()
        country = request.form['cnamess']
        data = covid.get_status_by_country_name(country)
        return render_template('covidworld.html',data=data,country=country,cnames = cnames) 

@app.route('/covidindia',methods = ['POST','GET'])
def covidindia():
    country = "India"
    snames = sname()
    covid = Covid()
    data = covid.get_status_by_country_name(country)
    total = data["confirmed"]
    cured = data["recovered"]
    death = data["deaths"]
    data = {"Total":total,"Cured":cured,"Death":death}
    state = "Entire India"
    return render_template('covidindia.html',data=data,state=state,snames = snames)

@app.route('/covidstates',methods = ['POST','GET'])
def covidstates():
    snames = sname()
    if request.method == 'POST':
        state = request.form['snamess']
        stats = states.getdata()
        data = stats[state]
        total = data["Total"]
        cured = data["Cured"]
        death = data["Death"]
        data = {"Total":total,"Cured":cured,"Death":death}
        return render_template('covidindia.html',data=data,state=state,snames = snames)
    # return render_template('covidindia.html',rows=rows)



@app.route('/coviddetails')
def coviddetails():
    # return render_template('coviddetails.html',rows=rows)
    return render_template('coviddetails.html')



if __name__ == "__main__":
    app.run(debug=True)