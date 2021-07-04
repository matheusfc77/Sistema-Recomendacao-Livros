import pandas as pd
from flask import Flask, request

cf_preds_df = pd.read_csv('filtering_recommendation.csv', index_col='ISBN')

class CFRecommender:
    
  MODEL_NAME = 'Collaborative Filtering'
  
  def __init__(self, cf_predictions_df, items_df=None):
    self.cf_predictions_df = cf_predictions_df
    self.items_df = items_df
      
  def get_model_name(self):
    return self.MODEL_NAME
      
  def recommend_items(self, user_id, items_to_ignore=[], topn=10):
    # Get and sort the user's predictions
    sorted_user_predictions = self.cf_predictions_df.loc[:, str(user_id)].sort_values(ascending=False)   \
                                .reset_index().rename(columns={str(user_id): 'recStrength'})

    # Recommend the highest predicted rating books that the user hasn't seen yet.
    recommendations_df = sorted_user_predictions[~sorted_user_predictions['ISBN'].isin(items_to_ignore)] \
                            .sort_values('recStrength', ascending = False) \
                            .head(topn)
    
    return recommendations_df

app = Flask(__name__)

@app.route("/")
def verifica_api_online():
  return "API ONLINE v2.0", 200

@app.route('/prediction',methods = ['POST'])
def prediction():
  try:
    user_id = int(request.form['user_id'])
    cf_recommender_model = CFRecommender(cf_preds_df)
    prediction = cf_recommender_model.recommend_items(user_id).ISBN
    prediction_json = prediction.to_json(orient="split", indent=4, index=False)
    return prediction_json
    
  except:
    return 'Error', 500

if __name__ == '__main__':
  app.run(debug = True)