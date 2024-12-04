import matplotlib.pyplot as plt

label = ['A','B','C','D']
num = [20, 17, 8, 40]

plt.bar(label, num)
plt.savefig('./bar.png')