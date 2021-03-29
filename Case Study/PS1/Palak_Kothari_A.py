def plot_payoff():

	# Import our modules that we are using
	import matplotlib.pyplot as plt

	# Create the vectors X and Y
	x = list(range(100))
	scale_factor = 10
	plt.xlim(0, 100)
	long_call=[]
	short_call = []
	long_put = []
	short_put=[]
	s1 = 50
	s2 = 50
	s3 = 50
	s4 = 50
	p1 = 4
	p2 = 4
	p3 = 2
	p4 = 2
	for i in range(len(x)):
	    long_call.append(max(i-s1, 0)-p1)
	    short_call.append(min(s2-i,0)+p2)
	    long_put.append(max(s3-i,0)-p3)
	    short_put.append(min(i-s4, 0)+p4)
	y=[]
	for i in range(len(x)):
	    y.append(short_call[i]+short_put[i])

	# Create the plot
	#plt.plot(x,y, color = "red", label = 'Total Payoff')
	plt.plot(x,long_call, linestyle = 'dashed', color = "blue", label = 'Payoff For Long Call', alpha = 0.5)
	plt.plot(x,short_call, linestyle = 'dashed', color = "orange", label = 'Payoff For Short Call', alpha = 0.5)
	plt.plot(x, long_put, linestyle = 'dashed', color = "green", label = 'Payoff For Long Put', alpha = 0.5)
	plt.plot(x, short_put, linestyle = 'dashed', color = "magenta", label = 'Payoff For Short Put', alpha = 0.4)

	# Add a title
	plt.title('Payoff Plots | Strike = $50')

	# Add X and y Label
	plt.xlabel('Stock Price ($)')
	plt.ylabel('Total Payoff')

	# Add a grid
	plt.grid(alpha=.4,linestyle='--')

	# Add a Legend
	plt.legend(loc ="lower center", prop={"size":8})

	# Show the plot
	plt.show()

if __name__ == "__main__":
	plot_payoff()