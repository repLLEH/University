from neural_network import *

if __name__ == '__main__':

    while(True):
        print('training = 1')
        print('recognize = 2')

        choice = (input())


        if int(choice) == 1:
            file_name = 'image.txt'
            models = readFromFile(file_name)
            matrix = getWeightFromModels(models)
            for i in matrix:
                print(i)
            matrix_file_name = 'matrix.txt'
            writeInFile(matrix_file_name, matrix)



        elif int(choice) == 2:
            model_file_name = 'image.txt'
            matrix_file_name = 'matrix.txt'
            matrix = getMatrix(matrix_file_name)
            model = readFromFile(model_file_name)

            run(model, matrix)


