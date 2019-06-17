""" 
	ARCHANA S M
	P180101CS
"""	
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
m_list = [] #mean of 10 samples

n=101
#--------Uniform Distribution---------
for i in range(1,n):			#repeat for 100 times
	
	s =np.random.uniform(0,1,5) 	#Create uniform distribution on interval (0,1) and draw sample of size 5
	mean = np.average(s)		 #find mean of 5 samples
	m_list.append(mean)		#mean append to a list m_list
	sd = np.std(s)
	#print  mean
	#print m_list

	if i == 2 or i == 10 or i == 50 or i== 100:
		plt.hist(m_list[0:i])
		plt.xlabel('x label')
		plt.ylabel('y label')
		plt.title("Plot1")
		plt.annotate('Iteration = {}'.format(i), [.2,1])
		plt.show()
	
for m in range(1,11):
	m_list1 = []			
	for i in range(1,n):
		
		z = np.random.uniform(0,1,m)  #Create uniform distribution on interval (0,1) and draw sample of size with varying m
		mean = np.average(z)	 #find mean of m samples
		m_list1.append(mean)	#mean append to a list m_list1
		#print  mean
		#print m_list1
	
	plt.hist(m_list1)
	plt.xlabel('x label')
	plt.ylabel('y label')
	plt.title("Plot 2: Sample Distribution varies with m")
	plt.annotate('m = {}'.format(m), [.2,1])
	plt.show()

#--------------poisson distribution-----------------
g_list = []

for i in range(1,n):#repeat for 10 times
	 
	g =np.random.poisson(5,5)#Create poisson distribution and 5 samples are drawn
	mean = np.average(g)   #find mean of 5 samples
	g_list.append(mean)	 #mean append to a list g_list
	#print  mean
	#print g_list
	if i == 2 or i == 10 or i == 50 or i== 100:
		plt.hist(g_list[0:i])
		plt.xlabel('x label')
		plt.ylabel('y label')
		plt.title("Plot3: Poisson Distribution")
		plt.annotate('Iteration = {}'.format(i), [1,2])
		plt.show()

for m in range(1,11):    #repeat for 10 times
	g_list1 = []
	for i in range(0,n): #repeat n times
		
		g = np.random.poisson(5,m)   #Create poisson distribution and draw sample of size with varying m
		mean = np.average(g)	#find mean of m samples
		g_list1.append(mean)    #mean append to a list g_list1
		#print  mean
		#print m_list
	plt.hist(g_list1)
	plt.xlabel('x label')
	plt.ylabel('y label')
	plt.title("Plot 4: Sample Distribution varies with m")
	plt.annotate('m = {}'.format(m), [3,2])
	plt.show()
