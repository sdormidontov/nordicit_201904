import cherrypy
import _pickle as cPickle
import numpy as np

class PredictGenerator(object):

    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head>
<style>
form {
  /* Center the form on the page */
  margin: 0 auto;
  width: 400px;
  /* Form outline */
  padding: 1em;
  border: 1px solid #CCC;
  border-radius: 1em;
}

form div + div {
  margin-top: 1em;
}

label {
  /* Uniform size & alignment */
  display: inline-block;
  width: 100px;
  text-align: right;
}

input, 
textarea {
  /* To make sure that all text fields have the same font settings
     By default, textareas have a monospace font */
  font: 1em sans-serif;

  /* Uniform text field size */
  width: 300px;
  box-sizing: border-box;

  /* Match form field borders */
  border: 1px solid #999;
}

input:focus, 
textarea:focus {
  /* Additional highlight for focused elements */
  border-color: #000;
}

textarea {
  /* Align multiline text fields with their labels */
  vertical-align: top;

  /* Provide space to type some text */
  height: 5em;
}

.button {
  /* Align buttons with the text fields */
  padding-left: 90px; /* same size as the label elements */
}

button {
  /* This extra margin represent roughly the same space as the space
     between the labels and their text fields */
  margin-left: .em;
}
</style>
</head> 
<form action="generate" method="get">
  <div>
    <label for="sepal_length">sepal_length:</label>
    <input type="text" id="sepal_length" name="sepal_length">
  </div>
  <div>
    <label for="sepal_width">sepal_width:</label>
    <input type="text" id="sepal_width" name="sepal_width">
  </div>
  <div>
    <label for="petal_length">petal_length:</label>
    <input type="text" id="petal_length" name="petal_length">
  </div>
  <div>
    <label for="petal_width">petal_width:</label>
    <input type="text" id="petal_width" name="petal_width">
  </div>
  <div class="button">
  <button type="submit">predict</button>
</div>
  
</form>      
        </html>
        """

    @cherrypy.expose
    def generate(self, sepal_length, sepal_width, petal_length, petal_width):
        with open('iris.pkl', 'rb') as fid:
            dt = cPickle.load(fid)

        sample = np.array([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])

        predict_string = 'predicted class = {}'.format(dt.predict(sample)[0])
        cherrypy.session['predict'] = predict_string

        return predict_string



    @cherrypy.expose
    def display(self):
        return cherrypy.session['predict']

if __name__ == "__main__":
    conf = {
        '/': {
            'tools.sessions.on':True
        }
    }
    cherrypy.quickstart(PredictGenerator(), '/', conf)