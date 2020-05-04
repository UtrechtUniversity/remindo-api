remindoapi
=========

This package provides a Python interface for the `Remindo API
<http://paragin.com>`. Using this package you can extract the
majority of the read-only data from Paragin.


Dependencies
------------

This package depends on the following packages:

-  requests
-  Cryptodome
-  json

They can be installed using ``pip``.

.. code:: python
    sudo pip install -r requirements.txt

or if pipenv is installed

.. code:: python
    sudo pipenv install


If you want to contribute to this package, you will need the ``nose``
package as well.


Installation
------------

To install, run the following command from the top-level package
directory.

.. code:: python
    sudo python setup.py install


Getting Started
---------------

The first thing is to request an API key from Utrecht University's (UU) ITS services.
One person you could contact, if you believe you will be granted access authorization
is Patrick Van der Veer, system architect of UU's ITS. 

Once you have the API keys, you need to substitute your keys in the `config.ini` file,
before creating client instance to query Remindo.

.. code:: python
    from remindoapi import client
    rc = client.RemindoClient()


Examples
--------

This package provides a Python interface for many Remindo API methods.
Here are a few examples demonstrating how to access data on Remindo.

Clusters
~~~~~

Let's access the first book added to Goodreads! It is the book with id
1.

.. code:: python

    clusters = rc.

Once you have the ``GoodreadsBook`` instance for the book, you can
access data for the queried book.

.. code:: python

    >>> book.title
    u'Harry Potter and the Half-Blood Prince (Harry Potter, #6)'
    >>> authors = book.authors
    >>> authors[0].name
    u'J.K. Rowling'
    >>> book.average_rating
    u'4.49'

Studies
~~~~~~~

You can get information about an author as well.

.. code:: python

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

Recipes
~~~~~

User data can be retrieved by user id or username.

.. code:: python

    >>> user = gc.user(1)
    >>> user.name
    u'Otis Chandler'
    >>> user.user_name
    u'otis'
    >>> user.small_image_url
    u'http://d.gr-assets.com/users/1189644957p2/1.jpg'

Moments
~~~~~~

Let's find a group discussing Python and get more information about it.

.. code:: python

    >>> g = gc.find_groups("Python")
    >>> g = groups[0]
    >>> g['title']
    u'The Computer Scientists'
    >>> group = gc.group(g['id'])
    >>> group.description
    u'Only for Committed Self Learners and Computer Scientists Who are Starving for
    Information, and Want to Advance their Skills Through: Reading, Practicing and
    Discussion Computer Science and Programming Books.'

Results
~~~~~~

Goodreads API also allows to list events happening in an area.

.. code:: python

    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'

Items
~~~~~~

Goodreads API also allows to list events happening in an area.

.. code:: python

    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'

Statistics and reliabilities
~~~~~~

Goodreads API also allows to list events happening in an area.

.. code:: python

    >>> events = gc.list_events(21229)
    >>> event = events[0]
    >>> event.title
    u'Books and Cocktails'
    >>> event.address
    u'120 N. Front St.'
    >>> event.city
    u'Wrightsville'


Documentation
-------------

Read more about this package
`here <http://goodreads.readthedocs.org/en/latest/>`__.

Contribution
------------

If you find an API method that is not supported by this package, feel
free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.

License
-------

`MIT License <http://opensource.org/licenses/mit-license.php>`__

Acknowledgment
--------------

Thanks to `Paul Shannon <https://github.com/paulshannon>`__ for
providing 'goodreads' package at PyPI.

.. |Build Status| image:: http://img.shields.io/travis/sefakilic/goodreads.svg
   :target: https://travis-ci.org/sefakilic/goodreads
.. |Coverage Status| image:: http://img.shields.io/coveralls/sefakilic/goodreads.svg
   :target: https://coveralls.io/r/sefakilic/goodreads
.. |Documentation Status| image:: https://readthedocs.org/projects/goodreads/badge/?version=latest
   :target: https://readthedocs.org/projects/goodreads/?badge=latest
.. |Downloads| image:: https://img.shields.io/pypi/dm/goodreads.svg
   :target: https://pypi.python.org/pypi/goodreads/
.. |Latest Version| image:: https://img.shields.io/pypi/v/goodreads.svg
   :target: https://pypi.python.org/pypi/goodreads/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/goodreads.svg
   :target: https://pypi.python.org/pypi/goodreads/
.. |License| image:: https://img.shields.io/pypi/l/goodreads.svg
   :target: https://pypi.python.org/pypi/goodreads/
