import numpy as np
import keras
import tensorflow as tf
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
seq = [('X^3', list(map(lambda x: x*x*x, [i for i in range(10)]))),
        ('x+1', [i for i in range(10)]),
        ('fibonacci', [fibonacci(10)])]
def sequence(seq_data):
    list = [0, 0, 0, 0]
    list[0] = seq_data[0]
    list[1] = seq_data[1]
    list[2] = seq_data[2]
    list[3] = seq_data[3]
    inp_layer = np.array(list)
    inp_layer = np.array(inp_layer[2])
    return inp_layer
def make_smth(seq_data):
    list = [0, 0, 0, 0]
    list[0] = seq_data[0]
    list[1] = seq_data[1]
    list[2] = seq_data[2]
    list[3] = seq_data[3]
    inp_layer = np.array(list)
    list = inp_layer.reshape((inp_layer.shape[0], 2, 2, 1))
    return list
def lstm():
    lstm_model.add(keras.layers.TimeDistributed(keras.layers.convolutional.Conv1D(filters=64,  activation='tanh'),))
    lstm_model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))
    lstm_model.add(keras.layers.LSTM(50, activation='relu'))
    lstm_model.add(keras.layers.Dense(1))
    lstm_model.compile(loss='mse')
lstm_model = keras.models.Sequential()
lstm()
while(True):
    print("X^3===>1")
    print("X+1===>2")
    print("Fibonaci===>3")
    print("Exit===>0")
    choice=input()
    if (choice==1):
        inp_layer, list = sequence(seq[0]),make_smth(seq[0])
        inp_layer.reshape((1, 2, 2, 1))
        out_layer = np.array([seq[i] for i in range(3, len(seq[1]))])
        lstm_model.fit(list, out_layer, epochs=500, verbose=0)
        final = lstm_model.predict(inp_layer, verbose=0)
        #round(int(final), 2)
        print("Sequence: ",seq[0])
        print("Result ", inp_layer, ": ", round(int(final), 2))
    elif (choice == 2):
        inp_layer, list = sequence(seq[1]), make_smth(seq[1])
        inp_layer.reshape((1, 2, 2, 1))
        out_layer = np.array([seq[i] for i in range(3, len(seq[1]))])
        lstm_model.fit(list, out_layer, epochs=500, verbose=0)
        final = lstm_model.predict(inp_layer, verbose=0)
        # round(int(final), 2)
        print("Sequence: ", seq[1])
        print("Result ", inp_layer, ": ", round(int(final), 2))
    elif (choice == 3):
        inp_layer, list = sequence(seq[2]), make_smth(seq[2])
        inp_layer.reshape((1, 2, 2, 1))
        out_layer = np.array([seq[i] for i in range(3, len(seq[2]))])
        lstm_model.fit(list, out_layer, epochs=500, verbose=0)
        final = lstm_model.predict(inp_layer, verbose=0)
        # round(int(final), 2)
        print("Sequence: ", seq[2])
        print("Result ", inp_layer, ": ", round(int(final), 2))
    elif (choice == 0):
        exit(0)