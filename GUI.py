import neat


net = neat.nn.FeedForwardNetwork.create(config)


inputs= [0.7,08.9,0.5,0.6] 
output = [0.1,0.2,0.3,0.4]
# Train a neat AI using the inputs data without supervision
model = neat.nn.FeedForwardNetwork.create(net, config)
model.train(inputs, output)


    