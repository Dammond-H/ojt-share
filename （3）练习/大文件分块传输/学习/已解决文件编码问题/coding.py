import time

import numpy as np

if __name__ == '__main__':
    asi = []
    for i in range(2):
        fo = open("%s.txt" % (i+1),"rb")
        temp = []
        while True:
            data = fo.read(1024)
            print(data)
            if not data:
                break
            for item in data:
                temp.append(item)
        asi.append(temp)

    print(len(asi[0]))
    print(len(asi[1]))
    identity = np.identity(2)
    ones = np.ones((2,2))
    for i in range(1,ones.shape[1]):
        for j in range(ones.shape[0]):
            ones[i][j] = (j+1)**i
    B = np.vstack((identity,ones))
    D = np.array(asi)
    start = time.time()
    C = np.dot(B, D)
    end = time.time()
    print(C.shape)
    print("共花费%s" % (end - start))


