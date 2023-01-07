from HopfieldNet import *

if __name__ == '__main__':
    hopnet=HopfieldNetwork()
    while(True):
        print('training = 1')
        print('recognize = 2')
        choice = (input())
        if int(choice) == 1:
            file_name = 'images'
            models = hopnet.readFromFile(file_name)
            print(models)
            matrix = hopnet.getWeightFromModels(models)
            for i in matrix:
                print(i)
            matrix_file_name = 'matrix.txt'
            hopnet.writeInFile(matrix_file_name, matrix)
        elif int(choice) == 2:
            model_file_name = 'image1.txt'
            matrix_file_name = 'matrix.txt'
            matrix = hopnet.getMatrix(matrix_file_name)
            model = hopnet.readFromFile(model_file_name)

            hopnet.run(model, matrix)


