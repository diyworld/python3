import matplotlib.pyplot as plt
name = ['one', 'one', 'one', 'one', 'one', 'two']
ratio = [1,1,1,1,1,2]
plt.pie(ratio, labels=name, colors=['b', 'r', 'g', 'k', 'c', 'm'])
plt.axis('equal')
plt.show()
