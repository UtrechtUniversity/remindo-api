Remindo API
=========

This package provides a Python interface for the API endpoint offered by [Remindo](https://www.paragin.nl/remindotoets/), a product of [Paragin](https://paragin.nl). This API wrapper allows you to extract and read the
majority of the exam-related data from Remindo. 

This package was developed by Utrecht University and is meant to be used with a read-only access. Therefore, the API features to modify exam-related data are not currently available.


Dependencies
------------

The package contains the following dependencies:

-  `requests`. To communicate with the API endpoint.
-  `Cryptodome`. To encrypt and decrypt data.
-  `json`. To read data.

The dependecies can be installed preferably using ``poetry`` but also using ``pip``. This can be done as follows.

Installing
------------


### Poetry

On terminal, after navigating to the repository:

```python
    poetry install
```

If you want to make changes to the code, please install the repository in "developer mode":

```python
    poetry install --dev
```

### Pip

On terminal, after navigating to the repository, install the requirements:

```python
    pip install remindo-api
```

If you want to make changes to the code, please install the requirements first:

```python
    pip install -r requirements.txt
    pip install remindo-api
```


Getting Started
---------------

The first thing is to request an API key from Utrecht University's (UU) ITS services.
One person you could contact, if you believe you will be granted access authorization
is Patrick Van der Veer, system architect of UU's ITS.

Once you have the API keys, you need to substitute your keys in the `config.cfg` file,
before creating any client instance to query the Remindo database.


Documentation
-------------

Read more about this package
[here](http://remindo.readthedocs.org/en/latest/).


Examples
--------

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
    clusters = rc.
```

Once you have the `cluster` instance, you can
access data for the queried book.

```python
    >>> book.title
    u'Harry Potter and the Half-Blood Prince (Harry Potter, #6)'
    >>> authors = book.authors
    >>> authors[0].name
    u'J.K. Rowling'
    >>> book.average_rating
    u'4.49'
```

### Retrieving Studies

You can get information about an author as well.

```python
    list_recipes = []
    [list_recipes.append(recipe.rid) for recipe in cln.list_recipes(cln, full = True)]

    # For results statistics
    for recipe in list_recipes[1:2]:
        # print(cln.list_stats(cln, recipe_id = recipe))
        print([i.p for i in cln.list_stats(cln, recipe_id = recipe)])

    # For item results
    # for recipe in list_recipes[1:2]:
    #     print([item.duration for item in cln.list_itemresults(cln, recipe_id = recipe, add_item_info = True)])
    # print(cln.list_itemresults(cln, recipe_id = recipe, add_item_info = True))

    # For reliability
    # for recipe in list_recipes:
    #     print(cln.list_reliability(cln, recipe_id = recipe))

    # For results
    # for recipe in list_recipes[1:2]:
    #     result_recipe = cln.list_results(cln, recipe_ids= recipe)
    #     print([[r.i_correct,r.i_answered]  for r in result_recipe])

    >>> author = gc.author(2617)
    >>> author.name
    u'Jonathan Safran Foer'
    >>> author.works_count
    u'13'
    >>> author.books
    [Extremely Loud and Incredibly Close, Everything Is Illuminated, Eating Animals, Tree of Codes, Everything is Illuminated & Extremely Loud and Incredibly Close, The unabridged pocketbook of lightning, The Future Dictionary of America, A Convergence of Birds: Original Fiction and Poetry Inspired by Joseph Cornell, New American Haggadah, The Sixth Borough]
```

### Retrieving Recipes

User data can be retrieved by user id or username.

```python
    >>> user = gc.user(1)
    >>> user.name
    u'Otis Chandler'
    >>> user.user_name
    u'otis'
    >>> user.small_image_url
    u'http://d.gr-assets.com/users/1189644957p2/1.jpg'
```

### Retrieving Moments

Let's find a group discussing Python and get more information about it.

```python
    >>> g = gc.find_groups("Python")
    >>> g = groups[0]
    >>> g['title']
    u'The Computer Scientists'
    >>> group = gc.group(g['id'])
    >>> group.description
    u'Only for Committed Self Learners and Computer Scientists Who are Starving for
    Information, and Want to Advance their Skills Through: Reading, Practicing and
    Discussion Computer Science and Programming Books.'
```

### Retrieving Results

Remindo API also allows to list events happening in an area.

```python
    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'
```

### Retrieving Items

Remindo API also allows to list events happening in an area.

```python
    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'
```

### Retrieving Items' Statistics and Reliabilities

Remindo API also allows to list events happening in an area.

```python
    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'
```

Contribution
------------

If you find an API method that is not supported by this package, feel
free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.

License
-------

[MIT License](http://opensource.org/licenses/mit-license.php).