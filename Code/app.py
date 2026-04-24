from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# LOGIN PAGE (FIRST PAGE)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid Username or Password")

    return render_template('login.html')

# Home Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Wazuh Dashboard
@app.route('/wazuh')
def wazuh():
    return redirect("https://192.168.56.101:5601")

# Logs Page (example)
@app.route('/logs')
def logs():
    return redirect("https://192.168.56.101:5601/app/wazuh#/overview/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&tab=general&tabView=panels&_a=(columns:!(_source),filters:!(('$state':(isImplicit:!t,store:appState),meta:(alias:!n,disabled:!f,index:'wazuh-alerts-*',key:manager.name,negate:!f,params:(query:siem),removable:!f,type:phrase),query:(match:(manager.name:(query:siem,type:phrase))))),index:'wazuh-alerts-*',interval:auto,query:(language:kuery,query:''),sort:!())")

# Agents Page
@app.route('/agents')
def agents():
    return redirect("https://192.168.56.101:5601/app/wazuh#/agents-preview/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(columns:!(_source),filters:!(('$state':(isImplicit:!t,store:appState),meta:(alias:!n,disabled:!f,index:'wazuh-alerts-*',key:manager.name,negate:!f,params:(query:siem),removable:!f,type:phrase),query:(match:(manager.name:(query:siem,type:phrase))))),index:'wazuh-alerts-*',interval:auto,query:(language:kuery,query:''),sort:!())")

# Settings Page
@app.route('/settings')
def settings():
    return redirect("https://192.168.56.101:5601/app/wazuh#/settings?tab=modules")

# Logout 
@app.route('/logout')
def logout():
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)