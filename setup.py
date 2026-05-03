from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirement=f.read().splitlines()
    
setup(
    name="Celebrity Detector and QA",
    version="0.1",
    auther="Nilesh",
    packages=find_packages(),
    install_requires=requirement
    
)    