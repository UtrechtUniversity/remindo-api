==========================
Remindo API Python Wrapper
==========================

.. toctree::
   :hidden:
   :maxdepth: 1

   reference

Python wrapper for `Remindo <https://www.paragin.com>`_.


Installation
=============

To install the Remindo API wrapper,
run this command in your terminal of choice:

.. code-block:: console

   $ pip install package/remindo_api


To install the Remindo API wrapper for development,
run this command in your terminal of choice:

.. code-block:: console

   $ pip install --dev package/remindo_api


Examples and Usage
==================

Here are a few examples demonstrating how to access data on Remindo.

Creating a Client instance
--------------------------

.. code-block:: python
   :linenos:

   from remindo_api import client
   rc = client.RemindoClient(
      config["REMINDOKEYS"]["UUID"],
      config["REMINDOKEYS"]["SECRET"],
      config["REMINDOKEYS"]["URL_BASE"],
   )

Check Connection
----------------

Let's use the `helloworld()` function to test if the credentials to connect to the Remindo endpoint are correct:

.. code-block:: python
   :linenos:

   hw = rc.helloworld()
   print(hw.message)
   >>> hello world

Once we determined that the credentials are correct, we can continue using the client to retrieve Remindo data.

Retrieving Clusters
-------------------

.. code-block:: python
   :linenos:

   clusters = rc.list_cluster()

Once you have retrieved a list of `cluster`, you can
access data for the queried clusters.

Let's access the first cluster of the list of clusters retrieved.

.. code-block:: python
   :linenos:

   clusters[0].rid
   '1111'
   clusters[0].name
   'cluster_name'

More details on the calls available in :ref:`cluster`.

Retrieving Studies
------------------

You can retrieve information about studies as well.

.. code-block:: python
   :linenos:
   
   studies = rc.list_studies()
   study = studies[0]

You can access information about a study as before:

.. code-block:: python
   :linenos:

   study.rid
   >>> 'rid'
   study.name
   >>> 'name'
   study.code
   >>> 'code'
   ...

More details on the calls available in :ref:`study`.

Retrieving Recipes
------------------

Recipes can also be retrieved with a simple call. In the example below we save a list of recipes to be used in later examples.

.. code-block:: python
   :linenos:

   list_recipes = []
   [list_recipes.append(recipe.rid) for recipe in rc.list_recipes(cln, full = True)]

The call uses the parameter `full = True` (by default is `False`) to indicate that we want to retrieve all the information available on Remindo concerning the Recipes.

More details on the calls available in :ref:`recipe`.

Retrieving Moments
------------------

Using the list of recipes saved from the previous call, we can now retrieve information about moments contained in each recipe.

Let's access the rid of the first recipe

.. code-block:: python
   :linenos:

   recipe_rid = list_recipes[0].rid
   moments = rc.list_moments(recipe_ids = recipe_rid)

Once we have retrieved all the moments information for one recipe, we can access these information as usual. We also save the moment id, to be used in a later call.

.. code-block:: python
   :linenos:

   # To be used later in examples
   moment_rid = moments[0].rid
    
   moments[0].rid
   >>> 'moment_rid'
   moments[0].code
   >>> 'moment_code'
   moments[0].date_end
   >>> 'moment_date_end'
   ...

More details on the calls available in :ref:`moment`.

Retrieving Results
------------------

Using the previously saved recipes information, we can use the general call `list_results` to retrive results' information about recipes.

.. code-block:: python
   :linenos:

   for recipe in list_recipes[1:2]:
      result_recipe = rc.list_results(cln, recipe_ids= recipe)
      print([[r.i_correct,r.i_answered]  for r in result_recipe])

More details on the calls available for recipe results are available in :ref:`result`.

Using the previously saved moment id, we now retrieve results' informations on individual moments using the `list_moment_results` call.

.. code-block:: python
   :linenos:

   moment_results = rc.list_moments_results(id = moment_rid)
    
   moment_results[0].subscription_id
   >>> 'moment_subscription_id'
   moment_results[0].user_id
   >>> 'moment_user_id'
   moment_results[0].user_code
   >>> 'moment_user_code'
   ...

More details on the calls available in :ref:`result`.

Retrieving Items
----------------

.. code-block:: python
   :linenos:

   for recipe in list_recipes[1:2]:
      print([item.duration for item in rc.list_itemresults(
         recipe_id = recipe,
         add_item_info = True)]
      )
      print(cln.list_itemresults(recipe_id = recipe, add_item_info = True))

More details on the calls available for _item_ results are available in :ref:`item`.

Retrieving Items' Statistics and Reliabilities
----------------------------------------------

.. code-block:: python
   :linenos:

   for recipe in list_recipes:
      print(cln.list_reliability(recipe_id = recipe))

More details on the calls available for item statistics in :ref:`stats` and for item reliabilities in :ref:`reliability`.
