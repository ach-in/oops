from pylab import *
import random

plot([1,2,3,4])
plot([5,6,7,8])
plot([1,2,3,4], [1,4,9,16])
figure()
plot([1,2,3,4], [1,4,9,16], 'ro')
axis([0, 6, 0, 20])
title('Earnings')
xlabel('Days')
ylabel('Dollars')
figure()
xAxis = array([1,2,3,4])
print xAxis
test = arange(1,5)
print test
print test == xAxis
yAxis = xAxis**3
plot(xAxis, yAxis, 'ro')
figure()
vals = []
dieVals = [1,2,3,4,5,6]
for i in range(10000):
 vals.append(random.choice(dieVals)+random.choice(dieVals))
hist(vals, bins=11)
show() 

