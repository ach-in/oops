
 #Tell Python which local standard to use
import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
#Format ints according to local standard
def formatInt(i):
	return locale.format('%d', i, grouping = True)
from pylab import *
import random, math

def throwDarts(numDarts, shouldPlot):
	inCircle = 0
	estimates = []
	for darts in range(1, numDarts + 1, 1):
		x = random.random()
		y = random.random()
		if math.sqrt(x*x + y*y) <= 1.0:
			inCircle += 1
		if shouldPlot:
			piGuess = 4*(inCircle/float(darts))
			estimates.append(piGuess)
		if darts%1000000 == 0: #So I know it's making progress
			piGuess = 4*(inCircle/float(darts))
			dartsStr = locale.format('%d', darts, True)
			print ('Estimate with', formatInt(darts), 'darts:', piGuess)
	if shouldPlot:
		xAxis = arange(1, len(estimates)+1)
		semilogx(xAxis, estimates)
		titleString = 'Estimations of pi, final estimate: ' + str(piGuess)
		title(titleString)
		xlabel('Number of Darts Thrown')
		ylabel('Estimate of pi')
		axhline(3.14159)
	return 4*(inCircle/float(numDarts))
def findPi(numDarts, shouldPlot=False):
	piGuess = throwDarts(numDarts, shouldPlot)
	print ('Estimated value of pi with', formatInt(numDarts), 'darts:', piGuess)

findPi(10000, True)
# findPi(100000000)
show() 