import Door_Detect as dd
import os

# Main driver of the door detect script

def main():
    model = dd.load()
    # test_open(model)
    # test_close(model)
    acc_test(model)

def test_open(model):
    print('\n### DOOR OPEN IMAGE TEST ###\n')
    for i in range(1, 48):
        decision = 0.0
        file = 'images/open/open' + str(i) + '.jpg'
        try:
            decision = dd.detect(model, file)
        except:
            file = 'images/open/open' + str(i) + '.JPG'
            decision = dd.detect(model, file)
        finally:
            print(i, ' detected: ', decision)

def test_close(model):
    print('\n### DOOR CLOSE IMAGE TEST ###\n')
    for i in range(1, 48):
        decision = 0.0
        file = 'images/close/closed' + str(i) + '.jpg'
        try:
            decision = dd.detect(model, file)
        except:
            file = 'images/close/closed' + str(i) + '.JPG'
            decision = dd.detect(model, file)
        finally:
            print(i, ' detected: ', decision)

def acc_test(model):
    print('\n### TESTING DATASET ACCURACY ###\n')
    acc = 0.0
    testset = os.listdir('images/test')
    size = len(testset)
    for file in testset:
        decision = dd.detect(model, 'images/test/' + file)
        print (file, ' detected: ', decision)
        if decision == 'Closed' and file[0] == 'c':
            acc += 1
        elif decision == 'Open' and file[0] == 'o':
            acc += 1
    print('Accuracy: ', acc/size * 100, '%')

if __name__ == "__main__":
    main()