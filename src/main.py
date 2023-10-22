#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# src/main.py

import argparse

from src.utils.os import load_config
from src.utils.plot import plot_collective
from src.intel.collective import Collective


def run_menu() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description='✨ Choices ✨')
    parser.add_argument('-ct', dest='collective_today', action='store_true',
                        help='Forecast for the collective today.')
    parser.add_argument('-cm', dest='collective_monthly', action='store_true',
                        help='Forecast for the collective this month.')
    parser.add_argument('-cc', dest='collective_custom', action='store_true',
                        help='Forecast for the collective in a custom date range.')
    return parser

def run() -> None:

    env_vars = load_config()
    parser = run_menu()
    args = parser.parse_args()
    PRINT_PLOT = False

    # TODO: Add argument for city and country
    if args.collective_today:
        c = Collective(env_vars)
        c.get_collective_forecast_today()

    elif args.collective_monthly:
        c = Collective(env_vars)
        c.get_collective_forecast_monthly()
        # TODO: remove plot from here, add option to save/name
        if PRINT_PLOT:
            plot_collective(c.transit_index, "Collective Transit Index (monthly))")
    
    elif args.collective_custom:
        c = Collective(env_vars)
        c.get_collective_forecast_custom()
        # TODO: remove plot from here, add option to save/name
        if PRINT_PLOT:
            plot_collective(c.transit_index, "Collective Transit Index (daily))")
        
    else:
        parser.print_help()


if __name__ == "__main__":
    run()
