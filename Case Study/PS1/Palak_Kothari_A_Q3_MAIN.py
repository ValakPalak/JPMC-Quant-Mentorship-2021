def plot_payoff():

	# Library used for plotting
	import matplotlib.pyplot as plt

	# Create the vectors X and Y
	x = list(range(100))
	long_call1=[]
	short_call1 = []
	long_call2 = []
	short_call2=[]
	s1 = 50
	s2 = 54
	s3 = 58
	s4 = 54
	p1 = 4
	p2 = 4
	p3 = 4
	p4 = 4
	for i in range(len(x)):
	    long_call1.append(max(i-s1, 0)-p1)
	    short_call1.append(min(s2-i,0)+p2)
	    long_call2.append(max(i-s3, 0)-p3)
	    short_call2.append(min(s4-i, 0)+p4)
	y=[]
	for i in range(len(x)):
	    y.append(short_call1[i]+short_call2[i]+long_call1[i]+long_call2[i])

	axes = plt.gca()
	axes.set_ylim([-6,6])

	# Create the plot
	plt.plot(x,y, color = "red", label = 'Total Payoff')
	plt.plot(x,long_call1, linestyle = 'dashed', color = "blue", label = 'Payoff For Long Call 1', alpha = 0.5)
	plt.plot(x, long_call2, linestyle = 'dashed', color = "green", label = 'Payoff For Long Call 2', alpha = 0.5)
	plt.plot(x,short_call1, linestyle = 'dashed', color = "orange", label = 'Payoff For Short Call 1', alpha = 0.5)
	plt.plot(x, short_call2, linestyle = 'dashed', color = "orange", label = 'Payoff For Short Call 2', alpha = 0.4)

	# Add a title
	plt.title('Payoff Plots (Long Call Butterfly Strategy)')

	# Add X and y Label
	plt.xlabel('Stock Price ($)')
	plt.ylabel('Strategy Payoff')

	# Add a grid
	plt.grid(alpha=.4,linestyle='--')

	# Add a Legend
	plt.legend(loc ="lower right", prop={"size":8})

	plt.scatter(54,4, color = 'black')
	plt.annotate('({}, {})'.format(54,4), (54,4), horizontalalignment = 'left')
	plt.scatter(50,0, color = 'black')
	plt.annotate('({}, {})'.format(50,0), (50,0), horizontalalignment = 'right')
	plt.scatter(58,0, color = 'black')
	plt.annotate('({}, {})'.format(58,0), (58,0), horizontalalignment = 'left')

	print("Portfolio Includes:")
	print("A Long Call At Strike Price $50 and Premium of $4")
	print("A Long Call At Strike Price $58 and Premium of $4")
	print("Two Short Calls At Strike Price $50 and Premium of $4")

	# Show the plot
	plt.show()

if __name__ == "__main__":
	plot_payoff()