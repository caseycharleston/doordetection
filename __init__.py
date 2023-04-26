import Door_Detect as dd
import torch

# Main driver of the door detect script

def main():
    model = dd.load()
    # test_open(model)
    # test_close(model)

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

if __name__ == "__main__":
    main()