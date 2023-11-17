from model_performance import load_model, load_new_data, acuracia 

def test_model_accuracy_above_90():
    acuracia_atual = acuracia(load_model(), load_new_data())
    threshold = 0.90
    assert acuracia_atual >= threshold
