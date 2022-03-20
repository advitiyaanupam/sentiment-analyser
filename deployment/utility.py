import pandas as pd

def sentence_lookup(review_id):
    df = pd.read_csv("reviews_test_4000.csv") #C:\\Users\\anupam.a.yadav\\Documents\\AnupamDocs\\assignment\\fallabella\\sentiments_train_test_reviews\\
    df.set_index('review_id',inplace=True)
    df_dict =  df.to_dict()['review']
    try:
        return df_dict[review_id]
    except Exception as e:
        return "Please enter a valid key"

def pred_class(num):
    if num >= 0.5:
        return "positive"
    else: 
        return "negative"
