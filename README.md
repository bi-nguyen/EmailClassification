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


  ![image](https://user-images.githubusercontent.com/106424285/232962273-8fdb67ca-9bc6-45f0-bf0d-3add983ff001.png)


    
    
    - ANN:
  
![image](https://user-images.githubusercontent.com/106424285/232962217-08b617b6-8d42-4d36-9e06-4d785470aa29.png)

 - From two results above, i decided to use logistic . Because two models give the same accuracy but the model logistic regression help to save time computation.
# Experiment:
 - I built an application by pyqt5
  ![image](https://user-images.githubusercontent.com/106424285/232960794-743a226e-b0f6-4c7c-a012-e40ca636ef50.png)
 - Here, I use an email that is spam . As you can see that, My application also give Spam
