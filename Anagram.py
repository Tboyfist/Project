if __name__ == '__main__':
    print("Hello World")

    word = sorted('rac')
    alternatives = ['car','cat']

    for alt in alternatives:
        if word == sorted(alt):
            print
            altword = sorted('rac')
        else:
             altword = sorted('cat')
alternatives = ['car', 'cat']

for alt in alternatives:
    if word == sorted(alt):
        print ("True")
    else:
        print ("false")

