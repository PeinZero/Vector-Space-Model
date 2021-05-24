from flask import Flask, render_template
from form import Searching
from operations import processing_query
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
CURRENT_DIR = os.getcwd()

@app.route('/', methods=['GET', 'POST'])
def index():
    titles= None
    startings= None
    documents=None
    no_result = False
    alpha_value = 0
    
    form = Searching()

    if form.validate_on_submit():
        titles={}
        startings={}

        query = form.searched.data
        alpha_value = form.alpha.data
        if alpha_value == '':
            alpha_value = 0
        form.searched.data = ''

        # processing user query
        documents=processing_query(query)


        # for displaying documents on the front-page
        if documents[list(documents.keys())[0]] == 0:
            no_result = True
        else:
            for doc,cosine_value in documents.items():
                if cosine_value >= alpha_value and cosine_value != 0:
                    # Opening and Reading the short stories
                    file_name=CURRENT_DIR + '\ShortStories\\' + doc + '.txt'
                    f=open(file_name, "r", encoding='UTF8')
                    file_lines=f.readlines()

                    count=0
                    starting = ''

                    for line in file_lines:
                        if count == 0:
                            title=line.strip()
                            titles[doc]=title
                        else:
                            if line.strip() != '':
                                starting=starting + " " + line.strip()
                        count=count + 1
                        if count == 7:
                            break
                    startings[doc]=starting
                    f.close()

    return render_template('home.html', form=form, documents=documents, titles = titles, startings = startings, no_result = no_result, alpha_value = alpha_value)

@app.route('/story/<docID>', methods=['GET', 'POST'])
def stories(docID):
    file = "./Stories/" + docID + ".html"
    return render_template(file)

if __name__ == '__main__':
    app.run(debug=True)
