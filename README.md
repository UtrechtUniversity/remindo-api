[![Documentation Status](https://readthedocs.org/projects/remindo-api/badge/?version=latest)](https://remindo-api.readthedocs.io/en/latest/?badge=latest)

# Remindo API

This package provides a Python interface for the API endpoint offered by [Remindo](https://www.paragin.nl/remindotoets/), a product of [Paragin](https://paragin.nl). This API wrapper allows you to extract and read the majority of the exam-related data from Remindo.

This package was developed by Utrecht University and is meant to be used with a read-only access. Therefore, the API features to modify exam-related data are not currently available.

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Remindo API](#remindo-api)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
    - [Built with](#built-with)
  - [Dependencies](#dependencies)
  - [Installing](#installing)
    - [Poetry](#poetry)
    - [Pip](#pip)
  - [Getting Started](#getting-started)
  - [Documentation](#documentation)
  - [Examples](#examples)
    - [Creating a Client instance](#creating-a-client-instance)
    - [Check Connection](#check-connection)
    - [Retrieving Clusters](#retrieving-clusters)
    - [Retrieving Studies](#retrieving-studies)
    - [Retrieving Recipes](#retrieving-recipes)
    - [Retrieving Moments](#retrieving-moments)
    - [Retrieving Results](#retrieving-results)
    - [Retrieving Items](#retrieving-items)
    - [Retrieving Items' Statistics and Reliabilities](#retrieving-items-statistics-and-reliabilities)
  - [Contributing](#contributing)
  - [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About the Project

**Date**: Started January 2019

**Research Software Engineer**:

- Leonardo Jaya Vida (l.j.vida@uu.nl)

### Built with

- [Requests](https://requests.readthedocs.io/en/master/)

## Dependencies

The package contains the following dependencies:

- `requests`. To communicate with the API endpoint.
- `Cryptodome`. To encrypt and decrypt data.
- `json`. To read data.

The dependecies can be installed preferably using ``poetry`` but also using ``pip``. This can be done as explained in [Installing](#installing).

## Installing

### Poetry

On terminal, after navigating to the repository:

```bash
    poetry install
```

If you want to make changes to the code, please install the repository in "developer mode":

```bash
    poetry install --dev
```

### Pip

On terminal, after navigating to the repository, install the requirements:

```bash
    pip install remindo-api
```

If you want to make changes to the code, please install the requirements first:

```bash
    pip install -r requirements.txt
    pip install remindo-api
```

## Getting Started

The first thing is to request an API key from Utrecht University's (UU) ITS services.
One person you could contact, if you believe you will be granted access authorization
is Patrick Van der Veer, system architect of UU's ITS.

Once you have the API keys, you need to substitute your keys in the `config.cfg` file,
before creating any client instance to query the Remindo database.


## Documentation

Read more about this package
[here](http://remindo.readthedocs.org/en/latest/).


## Examples

This package provides a Python interface for many Remindo API methods.
Here are a few examples demonstrating how to access data on Remindo.

### Creating a Client instance

```python
    from remindo_api import client
    rc = client.RemindoClient(
        config["REMINDOKEYS"]["UUID"],
        config["REMINDOKEYS"]["SECRET"],
        config["REMINDOKEYS"]["URL_BASE"],
    )
```

### Check Connection

Let's use the `helloworld()` function to test if the credentials to connect to the Remindo endpoint are correct:

```python
    hw = rc.helloworld()
    print(hw.message)
    >>> hello world
```

Once we determined that the credentials are correct, we can continue using the client to retrieve Remindo data.

### Retrieving Clusters

```python
    clusters = rc.list_cluster()
```

Once you have retrieved a list of `cluster`, you can
access data for the queried clusters.

Let's access the first cluster of the list of clusters retrieved.

```python
    >>> clusters[0].rid
    >>> '1111'
    clusters[0].name
    >>> 'cluster_name'
```

More details on the calls available for `clusters` are available [here](https://readthedocs.com).

### Retrieving Studies

You can retrieve information about studies as well.

```python
    studies = rc.list_studies()
    study = studies[0]
```

You can access information about a study as before:

```python
    study.rid
    >>> 'rid'
    study.name
    >>> 'name'
    study.code
    >>> 'code'
    ...
```

More details on the calls available for `studies` are available [here](https://readthedocs.com).

### Retrieving Recipes

Recipes can also be retrieved with a simple call. In the example below we save a list of recipes to be used in later examples.

```python
    list_recipes = []
    [list_recipes.append(recipe.rid) for recipe in rc.list_recipes(cln, full = True)]
```

The call uses the parameter `full = True` (by default is `False`) to indicate that we want to retrieve all the information available on Remindo concerning the Recipes.

More details on the calls available for `recipes` are available [here](https://readthedocs.com).

### Retrieving Moments

Using the list of recipes saved from the previous call, we can now retrieve information about moments contained in each recipe.

Let's access the rid of the first recipe

```python
    recipe_rid = list_recipes[0].rid
    moments = rc.list_moments(recipe_ids = recipe_rid)
```

Once we have retrieved all the moments information for one recipe, we can access these information as usual. We also save the moment id, to be used in a later call.

```python
    # To be used later in examples
    moment_rid = moments[0].rid
    moments[0].rid
    >>> 'moment_rid'
    moments[0].code
    >>> 'moment_code'
    moments[0].date_end
    >>> 'moment_date_end'
    ...
```

More details on the calls available for `moments` are available [here](https://readthedocs.com).

### Retrieving Results

Using the previously saved recipes information, we can use the general call `list_results` to retrive results' information about recipes.

```python
    for recipe in list_recipes[1:2]:
        result_recipe = rc.list_results(cln, recipe_ids= recipe)
        print([[r.i_correct,r.i_answered]  for r in result_recipe])
```

More details on the calls available for `recipes`' results are available [here](https://readthedocs.com).

Using the previously saved moment id, we now retrieve results' informations on individual moments using the `list_moment_results` call.

```python
    moment_results = rc.list_moments_results(id = moment_rid)
    moment_results[0].subscription_id
    >>> 'moment_subscription_id'
    moment_results[0].user_id
    >>> 'moment_user_id'
    moment_results[0].user_code
    >>> 'moment_user_code'
    ...
```

More details on the calls available for `moments`' results are available [here](https://readthedocs.com).

### Retrieving Items

```python
    for recipe in list_recipes[1:2]:
        print([item.duration for item in rc.list_itemresults(
            recipe_id = recipe,
            add_item_info = True)]
        )
        print(cln.list_itemresults(recipe_id = recipe, add_item_info = True))
```

More details on the calls available for `items`' results are available [here](https://readthedocs.com).

### Retrieving Items' Statistics and Reliabilities

```python
    for recipe in list_recipes:
        print(cln.list_reliability(recipe_id = recipe))
```

More details on the calls available for `items`' statistics and `reliabilities` are available [here](https://readthedocs.com).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Leonardo Vida - [@leonardojvida](https://twitter.com/leonardojvida) - l.j.vida@uu.nl

Project Link: [https://github.com/UtrechtUniversity/remindo-api](https://github.com/UtrechtUniversity/remindo-api)
