from matplotlib import pyplot as plt
import sys

sys.path.append('../')
import plotin1 as pi1


N = 50
x = np.concatenate((np.random.random(N) * 10, (np.random.random(N) * 10 + 10)))
y = np.concatenate((np.random.random(N) * 10, (np.random.random(N) * 10 + 10)))
tag = np.array(np.sign(x+y-20))

if __name__ == "__main__":
    plt = PointChart(x, y, tag)
    plt.show()