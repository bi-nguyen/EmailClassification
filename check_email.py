import pickle
from utils import preprocessing
import time
# from model import cv
cv=pickle.load(open("cv_Email_parameters.pkl","rb"))
model = pickle.load(open("Email_parameters.pkl","rb"))


def email(email):

    mail=[preprocessing(email)]
    input_data_feature=cv.transform(mail)
    prediction = model.predict(input_data_feature)
    if prediction==1:
        return "Spam"
    else:
        return "Ham"



def main():
    start = time.time()
    input_mail=open("mail.txt")
    mail=input_mail.read()
    print(email(mail))
    end = time.time()
    print(end-start)
    return

if __name__ == "__main__":
    main()