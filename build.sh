#!/bin/bash

# Install system dependencies
apt-get update
apt-get install -y libyaml-dev

# Upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

# Install Python dependencies
pip install -r requirements.txt
