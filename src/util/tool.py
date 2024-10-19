import yaml


def read_data_from_yaml(file_name):

    with open(file_name, "r") as stream:
        data = yaml.safe_load(stream=stream)
    return data
