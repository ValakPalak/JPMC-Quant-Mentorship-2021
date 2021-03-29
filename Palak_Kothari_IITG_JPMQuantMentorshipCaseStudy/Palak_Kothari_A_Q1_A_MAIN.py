def plot_payoff():
	# Import matplotlib module to plot the graph 
	import matplotlib.pyplot as plt

	# Create the vectors X and Y
	x = list(range(100))
	long_call=[]
	short_put=[]
	for i in range(len(x)):
	    long_call.append(max(i-50, 0)-4)
	    short_put.append(min(i-50, 0)+2)
	y=[]
	for i in range(len(x)):
	    y.append(long_call[i]+short_put[i])

	# Create the plot
	plt.plot(x,y, color = "red", label = 'Total Payoff')
	plt.plot(x,long_call, linestyle = 'dashed', color = "blue", label = 'Payoff For Long Call', alpha = 0.5)
	plt.plot(x, short_put, linestyle = 'dashed', color = "green", label = 'Payoff For Short Put', alpha = 0.5)
	
	# Add a title
	plt.title('Long a Call & Short a Put | Strike = $50')

	# Add X and y Label
	plt.xlabel('Stock Price ($)')
	plt.ylabel('Total Payoff')

	# Add a grid
	plt.grid(alpha=.4,linestyle='--')

	# Add a Legend
	plt.legend(loc ="lower right", prop={"size":12})

	# Show the plot
	plt.show()

if __name__ == "__main__":
	plot_payoff()
