# lemonade
A Scaffold for Containernet Tool - Build Python Files with One Configuration File

## Usage
### 1. Install Containernet
More details: https://containernet.github.io/#installation 
```bash
sudo apt-get install ansible git aptitude
git clone https://github.com/containernet/containernet.git
cd containernet/ansible
sudo ansible-playbook -i "localhost," -c local install.yml
```
### 2. Add Lemonade as a submodule
First change the current directory to the main folder of Containernet.
While being there, add the lemonade as a submodule. Change the directory to Lemonade. 
```bash
cd containernet
git submodule add https://github.com/CautiousLemons/lemonade.git
cd lemonade
```
### 3. Describe the network in JSON file
define the `sample.json` file and run the `__init__.py` script. Check the console for outputs.