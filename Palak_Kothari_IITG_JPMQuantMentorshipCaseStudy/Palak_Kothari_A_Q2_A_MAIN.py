def plot_payoff():

	# Import our modules that we are using
	import matplotlib.pyplot as plt

	# Create the vectors X and Y
	x = list(range(100))
	short_call = []
	short_put=[]
	s2 = 50
	s4 = 50
	p2 = 4
	p4 = 2

	for i in range(len(x)):
	    short_call.append(min(s2-i,0)+p2)
	    short_put.append(min(i-s4, 0)+p4)
	y=[]
	for i in range(len(x)):
	    y.append(short_call[i]+short_put[i])

	# Create the plot
	plt.plot(x,y, color = "red", label = 'Total Payoff')
	plt.plot(x,short_call, linestyle = 'dashed', color = "blue", label = 'Payoff For Short Call', alpha = 0.5)
	plt.plot(x, short_put, linestyle = 'dashed', color = "orange", label = 'Payoff For Short Put', alpha = 0.4)

	# Add a title
	plt.title('Combination of Short Put and Short Call')

	# Add X and y Label
	plt.xlabel('Stock Price ($)')
	plt.ylabel('Total Payoff')

	# Add a grid
	plt.grid(alpha=.4,linestyle='--')

	# Add a Legend
	plt.legend(loc ="lower center", prop={"size":8})

	# Show the plot
	plt.show()

	print("Portfolio Includes:")
	print("A Short Call At Strike Price 50 and A Short Put At Strike Price 50")

if __name__ == "__main__":
	plot_payoff()