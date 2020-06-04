import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

masAvr = []
def get_AP_Time(count):
    masRandom = []
    masTime = []
    masTmp = []
    average = 0

    print("---", count, "---")

    print("---append---")
    rndNumber = 1000000
    for item in range(count):
        start = time.time()
        masRandom.append(random.randrange(rndNumber))
        end = time.time()
        dis = end - start
        average += dis
        masTime.append(dis)

    print("Summary time = " + str(average))
    print("Average time = " + str(average/count))

    fig = plt.figure()
    fig.suptitle("append " + str(count), fontsize=20)
    plt.plot(range(count), masTime)
    plt.show()

    masTmp = masTime.copy()

    print("---pop---")

    masTime = []
    for item in range(count):
        start = time.time()
        masRandom.pop()
        end = time.time()
        dis = end - start
        average += dis
        masTime.append(dis)

    print("Summary time = " + str(average))
    print("Average time = " + str(average/count))

    fig = plt.figure()
    fig.suptitle("pop " + str(count), fontsize=20)
    plt.plot(range(count), masTime)
    plt.show()

    start = time.time()
    dis = masTmp.pop(int(count/2))
    end = time.time()
    masAvr.append(dis)
    print("Get average value time = " + str(dis))



get_AP_Time(100) #100
get_AP_Time(1000) #1000
get_AP_Time(10000) #10000
get_AP_Time(100000) #100000

fig = plt.figure()
fig.suptitle("Avr " + str(4), fontsize=20)
plt.plot(range(len(masAvr)), masAvr)
plt.show()





"""copy"""
print("---copy---")
copyCount = 1000000

masCopyNumbers = [50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000]
masAvrTimeCopy = []

for x in masCopyNumbers:
    masCopy = random.sample(range(x), x-1)
    start = time.time()
    masCopyTmp = masCopy.copy()
    end = time.time()
    dis = end - start
    print("Copy time for (", x, ") = ", dis)
    masAvrTimeCopy.append(dis)

print("Summary copy time = ", np.sum(masAvrTimeCopy))

fig = plt.figure()
fig.suptitle("copy", fontsize=20)
plt.plot(masCopyNumbers, masAvrTimeCopy)
plt.show()