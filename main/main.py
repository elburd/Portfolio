from flask import Flask, render_template
import helper_funcs as help

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects', methods=['GET', 'PUT'])
def projects():
    proj_list = help.get_project_list()
    return render_template('projects.html', proj_list=proj_list, )

@app.route('/projects/<proj_name>')
def project_page(proj_name: str):
    return render_template(f'project-{proj_name.lower()}.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)