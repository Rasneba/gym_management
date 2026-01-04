#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run Odoo
python3 odoo-bin -c odoo.conf -u all --dev=reload
