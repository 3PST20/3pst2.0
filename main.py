# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, url_for


import main

app = Flask(__name__)
# route -> site/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/<hostname>')
def device(hostname):
    if hostname in routers:
        return 'hostname inválido'
        #@app.errorhandler(404)
        #def invalid_route(e):
        #   return render_template('% hostname')
    else:
        return render_template(hostname)

routers = ['r1']
for router in routers:
    #with app.test_request_context():
        #print(url_for('device', hostname=router))
        print('')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)     #permite que as edições do código sejam automaticamente atualizadas

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
