import pandas as pd
from numpy import load
from flask import Flask, request

books = pd.read_csv('clean_books.csv')

data = books.reset_index()
books_series = pd.Series(data.index, index=data['ISBN'])

dict_cos_sim = load('cos_sim.npz')
cos_sim = dict_cos_sim['arr_0']

def get_recommendations(book, cosine_sim=cos_sim):
  try:
    idx = books_series[book]
    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]

    return books_series.iloc[book_indices].index

  except:
    return 0

app = Flask(__name__)

@app.route("/")
def verifica_api_online():
  return "API ONLINE v1.0", 200

@app.route('/prediction',methods = ['POST'])
def prediction():
    try:
        bookUser = request.form['book']
        prediction = get_recommendations(bookUser).to_frame().iloc[:, 0]
        prediction_json = prediction.to_json(orient="split", indent=4, index=False)
        return prediction_json
    
    except:
        return 'Error', 500

if __name__ == '__main__':
   app.run(debug = True)