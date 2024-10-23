import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df=pd.read_csv('demo.csv')

nominal_features=['x1','x2']
continous_features=['x3','x4','x5','x6']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'),continous_features),
        ('cat', Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),
                               ('onehot',OneHotEncoder())]),nominal_features)
])

df['x7']=np.random.rand(len(df))

X=df.drop(columns='y')
y=df['y']

scaler=StandardScaler()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

logistic_pipeline=Pipeline(steps=[('preprocessor', preprocessor),
                                  ('scaler',scaler),
                                  ('logistic',LogisticRegression())])


tree_pipeline=Pipeline(steps=[('preprocessor', preprocessor),
                                  ('scaler',scaler),
                                  ('logistic',DecisionTreeClassifier())])


forest_pipeline=Pipeline(steps=[('preprocessor', preprocessor),
                                  ('scaler',scaler),
                                  ('logistic',RandomForestClassifier())])

logistic_pipeline.fit(X_train,y_train)
tree_pipeline.fit(X_train,y_train)
forest_pipeline.fit(X_train,y_train)

y_pred_logistic=logistic_pipeline.predict(X_test)
y_pred_tree=tree_pipeline.predict(X_test)
y_pred_forest=forest_pipeline.predict(X_test)

def evaluate_model(y_test,y_pred,model_name):
    accuracy=accuracy_score(y_test,y_pred)
    f1=f1_score(y_test,y_pred)

    print(f"{model_name} Accuracy :  {accuracy:.4f}")
    print(f"{model_name} F1 score : {f1:.4f}")
    return accuracy,f1

print("\n Model Performance : ")

acc_log, f1_log=evaluate_model(y_test,y_pred_logistic,'Logistic Regression')
acc_tree, f1_tree=evaluate_model(y_test,y_pred_tree,"Decision Tree")
acc_forest, f1_forest=evaluate_model(y_test,y_pred_forest,'Random Forest')


def plot_confusion_matrix(y_test,y_pred,model_name):
    cm=confusion_matrix(y_test,y_pred)
    disp=ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(f'Confusion Matrix : {model_name}')
    plt.show()

print("\n Confusion Matrix : ")
plot_confusion_matrix(y_test,y_pred_logistic,"Logistic Regression")
plot_confusion_matrix(y_test,y_pred_tree,"Decision Tree")
plot_confusion_matrix(y_test,y_pred_forest,"Random Forest")