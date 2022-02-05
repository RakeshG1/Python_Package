from setuptools import setup 

setup(
    name="exampleWheel", # Package Name
    author="Example Package Wheel Creator", # Package Creator Name
    version="0.0.1", # Version of our package
    package_dir={"": "exampleWheel"},
    packages=["exampleWheel"] # Packages Name in which our python files with code logic
    # install_requires=['', ''], #external packages as dependencies
)