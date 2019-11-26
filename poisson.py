from scipy.stats import poisson
import matplotlib.pyplot as plt
plt.ylabel('Probability of car passing')
plt.xlabel('Number of cars')
plt.title('Probability of Distribution Curve')
arr=[]
rv=poisson(25)
for num in range(0,40):
    arr.append(rv.pmf(num))
prob=rv.pmf(28)
plt.grid(True)
plt.plot(arr,linewidth=2.0)
plt.plot([28],[prob],marker='o',markersize=6,color="red")
plt.show()
