# EmailClassification
# Packages:
  - pandas
  - scikitlearn
  - re
  - string
# Training:
 - For this project , I tested the data with two models:
    - LogisticRegression(solver='lbfgs',multi_class = 'multinomial',penalty='l2',C=10000000)
    - ANN(3 layers), for hidden layer  we took 50 nodes
 - Result:
  - Logistic Regression:
  
                    precision    recall  f1-score   support

               0       1.00      0.99      0.99       982
               1       0.98      1.00      0.99       467

        accuracy                           0.99      1449

    
    
  - ANN:
  
                      precision    recall  f1-score   support

               0       1.00      0.99      0.99       982
               1       0.97      1.00      0.98       467

        accuracy                           0.99      1449

 - From 2 results above, i decided to use logistic . Because two models give the same accuracy but the model logistic regression help to save time computation.
# Experiment:
 - I built an application by pyqt5
  ![image](https://user-images.githubusercontent.com/106424285/232960794-743a226e-b0f6-4c7c-a012-e40ca636ef50.png)
 - Here, I use an email that is spam . As you can see that, My application also give Spam
