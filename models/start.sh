#!/bin/bash

# Activate Python virtual environment
source venv/bin/activate

# Start Odoo
python3 odoo-bin -c odoo.conf -u all --dev=reload

