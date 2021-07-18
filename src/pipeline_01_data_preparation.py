import os
import argparse
import yaml
import logging


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="default") ## Passing Configuration 
    args.add_argument("--datasource", default=None) ## Passing Configuration 

    parsed_args = args.parse_args()
    print(parsed_args)
    print(parsed_args, parsed_args.datasource)
    print(parsed_args.config, parsed_args.datasource)  ## $python pipeline_01_data_preparation.py --config="Naren"

    