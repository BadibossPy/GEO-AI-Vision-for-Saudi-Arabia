#!/usr/bin/env python3
"""
Setup script for archaeological feature detection project.
Configures virtual environment and Jupyter kernel.
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run shell command and return result."""
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None

def setup_environment():
    """Set up virtual environment and Jupyter kernel."""
    print("Setting up environment...")
    
    # Create virtual environment
    print("Creating virtual environment...")
    run_command("python -m venv venv")
    
    # Activate and install requirements
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    print("Installing requirements...")
    run_command(f"{pip_cmd} install -r requirements.txt")
    
    # Install Jupyter kernel
    print("Installing Jupyter kernel...")
    run_command(f"{pip_cmd} install ipykernel")
    
    # Add kernel to Jupyter
    kernel_name = "archaeological-detection"
    run_command(f"{pip_cmd} install ipykernel")
    
    if os.name == 'nt':
        python_path = "venv\\Scripts\\python"
    else:
        python_path = "venv/bin/python"
    
    run_command(f"{python_path} -m ipykernel install --user --name {kernel_name} --display-name 'Archaeological Detection'")
    
    print(f"Setup complete!")
    print(f"Kernel '{kernel_name}' added to Jupyter")
    print(f"To use: jupyter lab notebooks/Archaeological_Feature_Detection.ipynb")

if __name__ == "__main__":
    setup_environment() 