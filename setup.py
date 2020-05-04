import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='remindo-api',
    description="Python wrapper for Remindo API",
    author='Leonardo Vida',
    author_email='lleonardovida@gmail.com',
    long_description=long_description,
    version='0.0.2',
    packages=setuptools.find_packages(),
    license='MIT',
    keywords = 'remindo API',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
    ]
)
