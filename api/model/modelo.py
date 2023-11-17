import numpy as np
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([form.lenght, 
                            form.depth, 
                            form.flipper, 
                            form.mass
                        ])

        # Aplica scaler nos dados assim como foi treinado no modelo
        X_input = X_input.reshape(1, -1)
        scaler = StandardScaler()
        rescaledEntradaX = scaler.fit(X_input)
        rescaledEntradaX = scaler.transform(X_input)
        
        identification = model.predict(rescaledEntradaX)
        return str(identification[0])