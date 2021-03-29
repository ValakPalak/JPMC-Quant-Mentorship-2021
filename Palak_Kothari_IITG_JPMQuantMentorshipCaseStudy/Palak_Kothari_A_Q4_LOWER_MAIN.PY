def plot_payoff():
	#Python Library for plotting
	import matplotlib.pyplot as plt

	# Create the vectors X and Y
	x = list(range(100))
	long_call=[]
	short_call = []
	lc1 = 50
	sc1 = 50.5
	p1 = 0
	p2 = 0

	for i in range(len(x)):
	    long_call.append(max(i-lc1, 0)-p1)
	    short_call.append(min(sc1-i,0)+p2)
	y=[]
	for i in range(len(x)):
	    y.append(short_call[i]+long_call[i]+short_call[i]+long_call[i])
	axes = plt.gca()
	axes.set_ylim([-0.5,1.5])
	# Create the plot
	plt.plot(x,y, color = "red", label = 'Strategy Payoff')
	# Add a title
	plt.title('Tighter Lower Bound')

	# Add X and y Label
	plt.xlabel('Stock Price ($)')
	plt.ylabel('Strategy Payoff')

	# Add a grid
	plt.grid(alpha=.4,linestyle='--')

	# Add a Legend
	plt.legend(loc ="lower right", prop={"size":12})

	#plt.text(50.5,1, '({}, {})'.format(50.5,1))
	plt.scatter(50.5,1, color = 'black')
	plt.annotate('({}, {})'.format(50.5,1), (50.5,1), horizontalalignment = 'right')
	plt.scatter(50,0, color = 'black')
	plt.annotate('({}, {})'.format(50,0), (50,0), horizontalalignment = 'left')

	print("Portfolio Includes:")
	print("A Long Call At Strike Price $50 and Premium of $0")
	print("A Short Call At Strike Price $50.5 and Premium of $0")

	# Show the plot
	plt.show()

if __name__ == '__main__':
	plot_payoff()