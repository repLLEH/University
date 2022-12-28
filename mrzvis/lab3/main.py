from Predict import Predict
def file_open_data_test(file_name,data_test,input_train,output_train):
    with open(file_name, 'r') as td:
        while True:
            out_train = []
            lines = td.readline()
            if not lines:
                break
            data_test += 1
            ipd, gt = lines.split("->")
            in_train = list(map(int, ipd.split(" ")))
            out_train.append(gt)
            out_train = list(map(int, out_train))
            input_train.append(in_train)
            output_train.append(out_train)
    td.close()
    return data_test
def file_open_input(file_name,data_test,input_train,output_train):
    with open(file_name, 'r') as td:
        while True:
            out_train = []
            lines = td.readline()
            if not lines:
                break
            data_test += 1
            ipd, gt = lines.split("->")
            in_train = list(map(int, ipd.split(" ")))
            out_train.append(gt)
            out_train = list(map(int, out_train))
            input_train.append(in_train)
            output_train.append(out_train)
    td.close()
    return input_train
def file_open_output(file_name,data_test,input_train,output_train):
    with open(file_name, 'r') as td:
        while True:
            out_train = []
            lines = td.readline()
            if not lines:
                break
            data_test += 1
            ipd, gt = lines.split("->")
            in_train = list(map(int, ipd.split(" ")))
            out_train.append(gt)
            out_train = list(map(int, out_train))
            input_train.append(in_train)
            output_train.append(out_train)
    td.close()
    return output_train

def main():
    sequence = Predict(lr=0.02, init_range=0.3)
    data = 0
    data_test = 0
    training_accuracy = 0
    testing_accuracy = 0
    input_train = []
    output_train = []
    input_test = []
    output_test = []


    data = file_open_data_test("train_data.txt",data_test,input_train,output_train)
    input_train = file_open_input("train_data.txt",data_test,input_train,output_train)
    output_train= file_open_output("train_data.txt",data_test,input_train,output_train)
    data_test=file_open_data_test("test_data.txt", data_test, input_test, output_test)
    input_test=file_open_input("test_data.txt", data_test, input_test, output_test)
    output_test=file_open_output("test_data.txt", data_test, input_test, output_test)
    print(input_train)
    print(output_train)
    for i in range(3000):
        cost = 0
        for j in range(len(input_train)):
            cost += sequence.train(input_train[j], output_train[j])
            
        if i % 100 == 0:
            correct = 0
            print('Epoch:', i)
            for k in range(len(input_train)):
                if sequence.predict(input_train[k]) == output_train[k]:
                    correct += 1
                training_accuracy = correct / data
            print('loss:', cost / data)
            print('train accuracy:', training_accuracy)

    correct_test = 0
    print('test result:')
    for l in range(len(input_test)):
        if sequence.predict(input_test[l]) == output_test[l]:
            correct_test +=1
        testing_accuracy = correct_test / data_test
    print('test accuracy', testing_accuracy)



    print([1, 2, 3], '->', sequence.predict([1, 2, 3]))
    print([3, 2, 1], '->', sequence.predict([3, 2, 1]))
    print([3, 2, 2], '->', sequence.predict([3, 2, 2]))
    print([0, 1, 0], '->', sequence.predict([0, 1, 0]))
    print([1, 2, 3, 4], '->', sequence.predict([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
