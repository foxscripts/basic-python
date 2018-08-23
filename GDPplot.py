from matplotlib import pyplot as plt 

years = [1956, 1961, 1966, 1974, 1979, 1985, 1990, 1997, 2002, 2007]
targetGDP = [2.1, 4.5, 5.6, 5.7, 4.4, 5.2, 5.0, 5.6, 6.5, 8.0]
actualGDP = [3.6, 4.1, 2.8, 3.3, 4.8, 5.7, 6.0, 6.8, 5.4, 7.2]

plt.plot(years, targetGDP, color='red', linewidth=5, label='Target GDP')
plt.plot(years, actualGDP, color='blue', linewidth=5, label='Actual GDP')

plt.title('India\'s GDP Growth Rate')
plt.xlabel('Years')
plt.ylabel('Growth rate of GDP in %')
plt.legend()
plt.grid(True, color='k')

plt.show()