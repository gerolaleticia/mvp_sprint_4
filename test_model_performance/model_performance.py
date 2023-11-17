import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def load_model():
    pickled_model = pickle.load(open('classificador.pkl', 'rb'))
    return pickled_model

def load_new_data():
    data = pd.read_csv('brand_new_test_data.csv')
    data = data.dropna() 
    return data

def acuracia(pickled_model, data):
    # trata os novos dados: separa variável target e colunas desnecessárias
    X = data.drop(['species', 'island', 'sex'], axis=1) 
    array_X = X.values
    X = array_X[:,0:8].astype(float)
    y = data['species'] # variavel target

    # padronização nos dados usando o mesmo scaler utilizado no modelo
    scaler = StandardScaler().fit(X)
    rescaledEntradaX = scaler.transform(X)

    predictions = pickled_model.predict(rescaledEntradaX)
    acuracia = accuracy_score(y, predictions)
    return acuracia