# lemonade
A Scaffold for Containernet Tool - Build Python Files with One Configuration File

##Usage
define the `sample.json` file and run the `__init__.py` script. Check the console for outputs.

##Sample Output
```python
info('*** Adding docker containers\n')
d1 = net.addDocker(ip="10.0.0.251", id="d1", dimage="ubuntu:trusty", name="my_iphone", )
d2 = net.addDocker(ip="10.0.0.252", id="d2", dimage="ubuntu:trusty", name="my_laptop", )
info('*** Adding docker containers\n')
d1 = net.addDocker(ip="10.0.0.251", id="d1", dimage="ubuntu:trusty", name="my_iphone", )
d2 = net.addDocker(ip="10.0.0.252", id="d2", dimage="ubuntu:trusty", name="my_laptop", )
``` 
