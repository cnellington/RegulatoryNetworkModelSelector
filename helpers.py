"""
Caleb Ellington
2020.02.10
"""

def parse_network(network_file):
    network = {}
    with open(network_file, 'r') as file:
        edges = file.readlines()
        for edge in edges:
            if edge == '\n':
                break
            edge = edge.strip('\n')
            (parent, child) = edge.split('->')
            if child not in network: network[child] = []
            if parent not in network: network[parent] = []
            network[child].append(parent)
    return network


def parse_data(data_file):
    data = {}
    with open(data_file, 'r') as file:
        experiments = file.readlines()
        for experiment in experiments:
            if experiment == '\n':
                break
            experiment = experiment.strip('\n')
            trials = experiment.split('\t')
            title = trials[0]
            values = trials[1:]
            data[title] = [int(x) for x in values]
    return data


def get_prob(data, target_values, given_values, verbose):
    """

    :param data:
    :param target_values: {targetname: targetvalue}
    :param given_values: {givenname: givenvalue, givenname: givenvalue}
    :return:
    """
    if given_values is None: given_values = {}
    if verbose: print(f"P(D{target_values}|θ{given_values})*")
    target_count = 0.0
    given_count = 0.0
    for i in range(len(data['EXP'])):
        include = True
        for given, given_value in given_values.items():
            include = include and data[given][i] == given_value
        if include:
            given_count += 1
            valid = True
            for target, target_value in target_values.items():
                valid = valid and data[target][i] == target_value
            if valid:
                target_count += 1
    prob = target_count / given_count
    return prob

def score_network(reverse_network, data, verbose=False):\
    # Get each combination of theta values
    if verbose: print("L(θ:D) = P(D|θ) =")
    m = len(data['EXP'])
    total_prob = 1.0
    for i in range(m):
        network_values= {}
        for key in reverse_network.keys():
            network_values[key] = data[key][i]

        for child, parents in reverse_network.items():
            target_values = {}
            given_values = {}
            target_values[child] = network_values[child]
            for parent in parents:
                given_values[parent] = network_values[parent]
            total_prob *= get_prob(data, target_values, given_values, verbose)

    return total_prob




