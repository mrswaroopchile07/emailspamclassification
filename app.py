{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0dfc8bce",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,url_for,request\n",
    "import pandas as pd \n",
    "import pickle\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "\treturn render_template('home.html')\n",
    "\n",
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "\tdf= pd.read_csv(\"spam.csv\", encoding=\"latin-1\")\n",
    "\tdf.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)\n",
    "\t# Features and Labels\n",
    "\tdf['label'] = df['class'].map({'ham': 0, 'spam': 1})\n",
    "\tX = df['message']\n",
    "\ty = df['label']\n",
    "\t\n",
    "\t# Extract Feature With CountVectorizer\n",
    "\tcv = CountVectorizer()\n",
    "\tX = cv.fit_transform(X) # Fit the Data\n",
    "\tfrom sklearn.model_selection import train_test_split\n",
    "\tX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)\n",
    "\t#Naive Bayes Classifier\n",
    "\tfrom sklearn.naive_bayes import MultinomialNB\n",
    "\n",
    "\tclf = MultinomialNB()\n",
    "\tclf.fit(X_train,y_train)\n",
    "\tclf.score(X_test,y_test)\n",
    "\t#Alternative Usage of Saved Model\n",
    "\t# joblib.dump(clf, 'NB_spam_model.pkl')\n",
    "\t# NB_spam_model = open('NB_spam_model.pkl','rb')\n",
    "\t# clf = joblib.load(NB_spam_model)\n",
    "\n",
    "\tif request.method == 'POST':\n",
    "\t\tmessage = request.form['message']\n",
    "\t\tdata = [message]\n",
    "\t\tvect = cv.transform(data).toarray()\n",
    "\t\tmy_prediction = clf.predict(vect)\n",
    "\treturn render_template('result.html',prediction = my_prediction)\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\tapp.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
