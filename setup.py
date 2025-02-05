from setuptools import setup, find_packages

setup(
    name="vuln_demo_math_ops",  
    version="1.0",        
    packages=find_packages(),
    author="Raghu",
    author_email="raghu@abc.com",
    description="An intentionally vulnerable Python package for testing vulnerability scanners..",
    install_requires=[
    	'Django==4.2.18',
	    'agpt==0.2.2',
	    'waitress==2.0.0',
	    'gradio==5.10.0',
	    'flask==1.0.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Adjust based on your Python version
)
