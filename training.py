import numpy as np
import pandas as pd
from utils import preprocessing 
from sklearn.feature_extraction.text import CountVectorizer

import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

df=pd.read_csv('./data/Spam Email raw text for NLP.csv',usecols=['CATEGORY','MESSAGE'])
df.rename(columns={"CATEGORY":"lable",'MESSAGE':'message'},inplace=True)
df['message']=df['message'].apply(lambda s: preprocessing(s))


# we just take 10000 popular words  from data
max_words = 10000
cv = CountVectorizer(max_features=max_words, stop_words='english')
sparse_matrix = cv.fit_transform(df['message']).toarray()

#data



# model logisticregression



# ANN from scikit learn
# model2=MLPClassifier(solver='lbfgs', alpha=0.01, hidden_layer_sizes=(100,100))
# model2.fit(x_train,y_train)




def main():
    x_train, x_test, y_train, y_test = train_test_split(sparse_matrix, np.array(df['lable']))
    model=LogisticRegression(solver='lbfgs',multi_class = 'multinomial',penalty='l2',C=10000000)
    model.fit(x_train,y_train)
    pickle.dump(model,open("Email_parameters.pkl","wb"))
    pickle.dump(cv,open("cv_Email_parameters.pkl","wb"))
    print(model.score(x_train,y_train))
    #print(model2.score(x_test,y_test))
    return

    



if __name__ == "__main__":
    main()