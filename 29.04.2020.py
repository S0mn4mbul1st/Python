import matplotlib.pyplot as plt


x1 = [1, 2, 3]
y1 = [2, 4, 1]

plt.plot(x1, y1,color='red', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12, label = "FirstDay")


x2 = [1, 2, 3]
y2 = [4, 1, 3]

plt.plot(x2, y2, label = "SecondDay")

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Testing')

plt.legend()
plt.show()



