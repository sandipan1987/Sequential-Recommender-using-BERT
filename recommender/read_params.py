import yaml

params_path = "./recommender/params.yaml"

def get_params(key):
    with open(params_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config[key]

if __name__ == "__main__":
    print("Test Works : " + get_params("data_source_zip"))