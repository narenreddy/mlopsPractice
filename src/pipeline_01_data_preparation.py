import os
import argparse
import yaml
import logging

def read_params(config_path): 
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path, datasource):
    config = read_params(config_path)
    print(config) 

if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("../config", "params.yaml") 
#    args.add_argument("--config", default="default") ## Passing Configuration 
    args.add_argument("--config", default=default_config_path) 
    args.add_argument("--datasource", default=None) ## Passing Configuration 

    parsed_args = args.parse_args()
    # print(parsed_args)
    # print(parsed_args, parsed_args.datasource)
    # print(parsed_args.config, parsed_args.datasource)  ## $python pipeline_01_data_preparation.py --config="Naren"
    main(config_path=parsed_args.config , datasource=parsed_args.datasource)
    