import mnist_loader
import network

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
print("load minist data")
print(type(training_data))
print(len(training_data))
print(training_data[0][0].shape)
print(training_data[0][1].shape)

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
