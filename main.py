import matplotlib.pyplot as plt

from data_handlers import Iris, MNIST, Penguins
from model import MLP
from util import get_logger, plot_mses

def penguins_run():
    penguins = Penguins("data/penguins.csv")
    model = MLP(
        *penguins.partition_data(),
        [8, 18, 12],
        bias=1,
        eta=0.4,
        mse_threshold=0.05,
        epochs=750,
    )
    mses, _ = model.train()
    plot_mses(mses)
    acc = model.test()
    print("Penguins Accuracy: ", acc)

def mnist_run():
    mnist = MNIST("data/mnist_train.csv", "data/mnist_test.csv")
    model = MLP(
        *mnist.partition_data(),
        [16, 16, 12],
        bias=1,
        eta=0.5,
        mse_threshold=0.15,
        epochs=10,
    )
    mses, _ = model.train()
    plot_mses(mses)
    acc = model.test()
    print("MNIST Accuracy: ", acc)

def iris_run():
    iris = Iris("data/iris.csv")
    model = MLP(
        *iris.partition_data(),
        [16, 12, 8],
        bias=1,
        eta=0.4,
        mse_threshold=0.05,
        epochs=100
    )
    mses, acc = model.train()
    print("Iris Train Accuracy:", acc)
    plot_mses(mses)
    acc = model.test()
    print("Iris Accuracy: ", acc)

if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Starting...")

    plt.style.use("ggplot")

    iris_run()

    logger.info("Finished.")