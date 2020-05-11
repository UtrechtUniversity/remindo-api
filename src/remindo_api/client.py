import requests

from .cluster import RemindoCluster
from .helloworld import RemindoHelloWorld
from .item import RemindoItem
from .moment import RemindoMoment
from .recipe import RemindoRecipe
from .reliability import RemindoReliability
from .request import RemindoRequest
from .result import RemindoResult
from .stats import RemindoStats
from .study import RemindoStudy


# TODO: Error: /api/v1/result/reliability {'error':
# 'Please specify a valid API method for class result. Available methods: list'}
# TODO: what about substituting to personal data fake with Faker?
# TODO: complete list_stubscritpion call


class RemindoClientException(Exception):
    """Class that is called for exception messages

    You can see the usage of this class looking at the test

    """

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class RemindoClient:
    """Main client class of Remindo
    """

    def __init__(self, uuid, secret, url_base):
        """Initialize the client"""
        self.uuid = uuid
        self.secret = secret
        self.url_base = url_base
        self.ip = requests.get("https://jsonip.com").json()["ip"]

    @property
    def query_dict(self):
        """ Query personal data from client """
        return {"key": self.uuid, "secret": self.secret, "url_base": self.url_base}

    def request(self, *args, **kwargs):
        """ Create a remindo_api object and make a request """
        req = RemindoRequest(self, *args, **kwargs)
        return req.request()

    def hello_world(self):
        """ Make a "Hello World" request to verify keys """
        resp = self.request(url="/remote_api/hello_world", content="")
        return RemindoHelloWorld(resp)

    def list_clusters(self, filter=None, category=None, full=True):
        """List all available user groups.

        Parameters
        ---------
        filter : string, optional
            A search query for the name of the cluster.
        category : string, optional
            Return only user groups in this category.
        full : boolean, optional
            Return all the user groups.

        Returns
        -------
        RemindoCluster : dict
            A list of dict of user groups in the form:
                {"id" : 0000, "name" : 'test'}.
        """
        params = {}
        if filter is not None:
            params["filter"] = filter
        if category is not None:
            params["category"] = category
        if full is not False:
            params["full"] = True

        resp = self.request(url="/cluster/list", content=params)
        categories = RemindoCluster(resp["clusters"]).categories()
        clusters = [
            RemindoCluster(clu) for cat in categories for clu in resp["clusters"][cat]
        ]
        return clusters

    def list_studies(
        self, code=None, study_id=None, datasource_uuid=None, complete=False, since=None
    ):
        """'List studies, which are a set of recipes

        Parameters
        ---------
        code : string, optional
            Return studies with study code
        study_id : int, optional
            Retrun study with ID
        datasource_uuid : string, optional
            Return studies from test manager with UUID
        complete : boolean, optional, default: false
            Full study & all recipes)
        since : date, optional
            Date is in Y-m-d format. To be filled only when complete is true

        Returns
        --------
        RemindoStudy : list
            Return list of Remindo studies
        RemindoRecipe : list
            if complete == True, return list of studies and associated recipes modified since date
        """
        params = {}
        if code is not None:
            params["code"] = code
        if study_id is not None:
            params["study_id"] = study_id
        if datasource_uuid is not None:
            params["datasource_uuid"] = datasource_uuid
        if complete is not False:
            params["complete"] = complete
        if since is not None:
            params["since"] = since

        list_study = list()
        resp = self.request(url="/study/list", content=params)
        studies = RemindoStudy(resp["studies"]).list_all()
        if complete is False:
            for study in studies:
                s = studies[study]
                s.update({"api_call_params": params})
                list_study.append(RemindoStudy(s))
            return list_study
        else:
            recipes = []
            for study in studies:
                s = studies[study]
                s.update({"api_call_params": params})
                list_study.append(RemindoStudy(s))
            for study in resp["studies"]:
                for recipe in resp["studies"][study]["recipes"]:
                    r = resp["studies"][study]["recipes"][recipe]
                    r.update({"api_call_params": params})
                    recipes.append(RemindoRecipe(r))
            return list_study, recipes

    def list_recipes(
        self,
        code=None,
        category=None,
        study_id=None,
        recipe_id=None,
        filtr=None,
        datasource_uuid=None,
        since=None,
        properties=None,
        full=False,
    ):
        """List recipes

        Recipe is a list of question for a determined exam - needs to be assigned
        to a student with a 'subscription' before starting exam.

        Parameters
        ---------
        code : string, optional
            When given, it will only return recipes where the recipe code contains the given text.
        category : string, optional
            When given, it will only return recipes where the recipe category contains the given text.
        study_id: int, optional
            When given, only the recipes in the study with this ID are returned.
        recipe_id : int, optional
            When given, only the recipe with the given ID is returned
        filter : filterobject, optional
            Search query for retrieving the recipe
        datasource_uuid : string, optional
            Return recipes from test manager with UUID
        since : date, Y-m-d format, optional
            Return recipes modified since
        properties : boolean, optional
            Returns the custom from test manager
        full : boolean, optional
            Returns additional information

        Returns
        -------
        RemindoRecipe : list
            Return list of Remindo recipe object(s)
        """
        params = {}
        if code is not None:
            params["code"] = code
        if category is not None:
            params["category"] = category
        if study_id is not None:
            params["study_id"] = int(study_id)
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if filtr is not None:
            params["filter"] = filtr
        if datasource_uuid is not None:
            params["datasource_uuid"] = datasource_uuid
        if since is not None:
            params["since"] = since
        if properties is not None:
            params["properties"] = properties
        if full is not False:
            params["full"] = True

        resp = self.request(url="/recipe/list", content=params)
        list_recipes = []
        for recipe in resp["recipes"]:
            r = resp["recipes"][recipe]
            r.update({"api_call_params": params})
            list_recipes.append(RemindoRecipe(r))

        return list_recipes

    def list_moments(self, ids=None, code=None, recipe_ids=None, frm=None, until=None):
        """List moments

        Parameters
        ---------
        ids : int or array<int>, optional
            Return moment for test id(s)
        codes : string or array<string>, optional
            Return list for test moment code(s)
        recipe_ids : int or array<int>, optional
            Return moments with recipe id(s)
        from : datetime string, optional
            Return moments after date
        until : datetime string, optional
            Return moments before date

        Returns
        -------
        RemindoMoment : list
            Return list of RemindoMoment object(s)
        """
        params = {}
        if ids is not None:
            params["ids"] = ids
        if code is not None:
            params["code"] = list(code)
        if recipe_ids is not None:
            params["recipe_ids"] = recipe_ids
        if frm is not None:
            params["from"] = frm
        if until is not None:
            params["until"] = until

        resp = self.request(url="/moment/list", content=params)
        # moments = RemindoMoment(resp["moments"]).list_all()
        list_moments = []
        for moment in resp["moments"]:
            m = resp["moments"][moment]
            m.update({"api_call_params": params})
            list_moments.append(RemindoMoment(m))

        return list_moments

    def list_moments_results(
        self,
        id=None,
        code=None,
        candidate_ids=None,
        candidate_codes=None,
        candidate_filter=None,
    ):
        """List results of selected moments

        Parameters
        --------.
        id : int, string mandatory
            ID of moment
        code : int, string mandatory
            code of moment
        candidate_ids : int or array<int>, optional
            Return result for candidate id
        candidate_codes : int or array<int>, optional
            Return result for candidate code(s)
        candidate_filter : filterobject, optional
            Filter object to retrieve user

        Returns
        -------
        RemindoResult : list
            Return list of Remindo Result object(s) for the moment.
        """
        params = {}
        if id is not None:
            params["id"] = id
        if code is not None:
            params["code"] = code
        if candidate_ids is not None:
            params["candidate_ids"] = list(candidate_ids)
        if candidate_codes is not None:
            params["candidate_codes"] = list(candidate_codes)
        if candidate_filter is not None:
            params["candidate_filter"] = candidate_filter

        resp = self.request(url="/moment/results", content=params)
        if resp["success"] is True:
            list_results = []
            for result in resp["results"]:
                result.update({"api_call_params": params})
                list_results.append(RemindoResult(result))
            return list_results
        if resp["success"] is False:
            return False

    def list_results(
        self,
        typ=None,
        modified_since=None,
        modified_until=None,
        start_time_since=None,
        start_time_until=None,
        end_time_since=None,
        end_time_until=None,
        status=None,
        search=None,
        candidate_ids=None,
        cluster_ids=None,
        study_ids=None,
        recipe_ids=None,
        result_ids=None,
        subscription_ids=None,
        page=None,
        page_size=None,
        complete=False,
    ):
        """Retrieve list of results

        Parameters
        ---------
        type : string, optional
            Restrict by type: practice, graded practice, exam
        modified_since : string/int, optional
            estrict by date and time of last modification
        modified_until : string/int, optional
            Restrict by date and time of last modification
        start_time_since : string/int, optional
            Restrict by date and time of start
        start_time_until : string/int, optional
            Restrict by date and time of start
        end_time_since : string/int, optional
            Restrict by date and time of end
        end_time_until : string/int, optional
            Restrict by date and time of end
        status : string, optional
            Restrict by results with status: started, finished, review, closed
        search : string, optional
            Restrict by recipe name or user name match
        candidate_ids : int/array<int>, optional
            Restrict by candidates IDs
        cluster_ids : int/array<int>, optional
            Restrict by clusters IDs
        study_ids : int/array<int>, optional
            Restrict by studies IDs
        recipe_ids : int/array<int>, optional
            Restrict by recipes IDs
        result_ids : int/array<int>, optional
            Restrict by results IDs
        subscription_ids : int/array<int>, optional
            Restrict by subscriptions IDs
        page : int, optional
            page to be requested, starting at 1
        page_size : int, optional
            Desirable page size, from 1 to 200
        complete : bool, optional
            Adds fields report_data and actionlog

        Returns
        -------
        RemindoResult : list
            If the results have more than one page of results, returns a list of RemindoResult objects
            If the results only have one page of results, returns one RemindoResult object.
        """
        params = {}
        if typ is not None:
            params["type"] = typ
        if modified_since is not None:
            params["modified_since"] = modified_since
        if modified_until is not None:
            params["modified_until"] = modified_until
        if start_time_since is not None:
            params["start_time_since"] = start_time_since
        if start_time_until is not None:
            params["start_time_until"] = start_time_until
        if end_time_since is not None:
            params["end_time_since"] = end_time_since
        if end_time_until is not None:
            params["end_time_until"] = end_time_until
        if status is not None:
            params["status"] = status
        if search is not None:
            params["search"] = search
        if candidate_ids is not None:
            params["candidate_ids"] = list(candidate_ids)
        if cluster_ids is not None:
            params["cluster_ids"] = list(cluster_ids)
        if study_ids is not None:
            params["study_ids"] = list(study_ids)
        if recipe_ids is not None:
            params["recipe_ids"] = recipe_ids
        if result_ids is not None:
            params["result_ids"] = list(result_ids)
        if subscription_ids is not None:
            params["subscription_ids"] = subscription_ids
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if complete is not False:
            params["complete"] = True

        resp = self.request(url="/result/list", content=params)
        if resp["success"] is True:
            page_dict = {
                "total_pages": resp["response"]["total_pages"],
                "total_results": resp["response"]["total_results"],
                "page_size": resp["response"]["page_size"],
                "current_page": resp["response"]["current_page"],
            }
            result_list = []
            if page_dict["total_pages"] > 1:
                for r in range(len(resp["response"]["results"])):
                    r_first = resp["response"]["results"][r]
                    # Add the api call params
                    r_first.update({"api_call_params": params})
                    result_list.append(RemindoResult(r_first))
                for i in range(1, page_dict["total_pages"]):
                    # Go to next page
                    params["page"] = i + 1
                    new_resp = self.request(url="/result/list", content=params)
                    for j in range(len(new_resp["response"]["results"])):
                        r_next = new_resp["response"]["results"][j]
                        # Add the api call params
                        r_next.update({"api_call_params": params})
                        result_list.append(RemindoResult(r_next))
                return result_list
            else:
                for r in range(len(resp["response"]["results"])):
                    r_unique = resp["response"]["results"][r]
                    # Add the api call params
                    r_unique.update({"api_call_params": params})
                    result_list.append(RemindoResult(r_unique))
                return result_list

    def list_subscription_result(
        self,
        recipe_id=None,
        moment_id=None,
        subscription_ids=None,
        user_ids=None,
        add_item_info=False,
    ):
        """List subscription results

        No more than 50.000

        Parameters
        ---------
        recipe_id : int, mandatory
            Recipe ID to retrive item result statistics.
        moment_id : int, optional
            Limit results to this moment.
        subscription_ids : array, optional
            Limit results to this subscription ID.
        user_ids : array, optional
            Limit results to user IDs.
        add_item_info : boolean, optional
            If true, and with single subscription_id or single user_id, add extra information for each item

        Returns
        -------
        list : list
            return results tied to subscription.
        """
        params = {}
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if moment_id is not None:
            params["moment_id"] = moment_id
        if subscription_ids is not None:
            params["subscription_ids"] = list(subscription_ids)
        if user_ids is not None:
            params["user_ids"] = list(user_ids)
        if add_item_info is not False:
            params["add_item_info"] = True
        resp = self.request(url="/itemresult/list", content=params)
        return resp

    # Behavior of this call is not consistent with the documentation
    def list_reliability(
        self,
        recipe_id=None,
        moment_id=None,
        variant_id=None,
        scan_id=None,
        corrections=None,
        locale=None,
    ):
        """"Calculate result reliability

        Calculate the reliability over a set of results using cronbach’s alpha
        and the standard error of measurement.You always need to filter on a single
        recipe to calculate the reliability. Either using a test moment, a recipe,
        a scan or a paper variant.

        Parameters
        ---------
        recipe_id : int, optional
            Calculate reliability for the given test recipe
        moment_id : int, optional
            Calculate reliability for the given test moment
        variant_id : int, optional
            Calculate reliability for the given paper variant
        scan_id : int, optional
            Calculate reliability for the given scan corrections
        corrections : enum[], optional
            Which answer model corrections to apply while calculating the reliability.
            Available are: \active (active corrections) or concept (concept corrections)
        locale : string, optional
            The language in which to provide extra information (notes)

        Returns
        -------
        alpha : float
            Cronbach's Alpha value
        sem : float
            SEM value
        notes : text
            text
        missing count : int
            int
        answer_count : int
            int
        stdev : float
            float
        average : float
            float
        max : int
            int
        error : bool
            true or null
        success : bool
            BOOL
        """

        params = {}
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if moment_id is not None:
            params["moment_id"] = moment_id
        if variant_id is not None:
            params["variant_id"] = int(variant_id)
        if corrections is not None:
            params["corrections"] = list(corrections)
        if locale is not None:
            params["locale"] = str(locale)

        resp = self.request(url="/result/reliability/list", content=params)
        resp.update({"api_call_params": params})
        return RemindoReliability(resp)

    def list_item_results(
        self,
        recipe_id=None,
        moment_id=None,
        subscription_ids=None,
        user_ids=None,
        add_item_info=False,
    ):
        """"Retrieve item results

        Returns a list of question/item results for a given filter. No more than 50.000
        item results will be returned. The result is a nested array, grouped by subscription
        id and test section (if applicable).

        Parameters
        ---------
        recipe_id : int, mandatory
            The recipe ID for which you want to retrieve the item result statistic
        moment_id : int, optional
            Limit the item results to the ones used in this moment
        subscription_ids : array, optional
            Limit the item results to the given subscription IDs
        user_ids : array, optional
            Limit the item results to the given user IDs
        add_item_info : boolean, optional
            If true, and in combination with a single subscription_id or a single user_id,
            will add extra information for each item, such as item properties, the author
            of the item and the time it was created

        Returns
        -------
        """

        params = dict()
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if moment_id is not None:
            params["moment_id"] = moment_id
        if subscription_ids is not None:
            params["subscription_ids"] = subscription_ids
        if user_ids is not None:
            params["user_ids"] = user_ids
        if add_item_info is not False:
            params["add_item_info"] = True

        resp = self.request(url="/itemresult/list", content=params)
        if resp["success"] is not False:
            resp = resp["itemresults"]
            itemresults = []
            for subscription in resp.keys():
                sections = len(resp[subscription])
                for s in range(sections):
                    # section = resp[subscription][s]["section"]
                    # section_id = resp[subscription][s]["section_id"]
                    items = resp[subscription][s]["itemresults"].keys()
                    for i in items:
                        it = resp[subscription][s]["itemresults"][i]
                        it.update({"api_call_params": params})
                        itemresults.append(RemindoItem(it))
            return itemresults
        else:
            return None

    def list_stats(
        self, recipe_id=None, moment_id=None, subscription_ids=None, user_ids=None
    ):
        """"Retrieve recipe question/item result statistics

        Returns a list of aggregated statistics for each question/item results for a given
        recipe of pair recipe-moment.

        Parameters
        ---------
        recipe_id : int, mandatory
            The recipe ID for which you want to retrieve the item result statistics
        moment_id : int, optional
            Limit the item results to the ones used in this moment.
        subscription_ids : array, optional
            Limit the item results to the given subscription IDs
        user_ids : array, optional
            Limit the item results to the given user IDs

        Returns
        -------
        """

        params = {}
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if moment_id is not None:
            params["moment_id"] = moment_id
        if subscription_ids is not None:
            params["subscription_ids"] = subscription_ids
        if user_ids is not None:
            params["user_ids"] = user_ids

        # Why does the call return results within a list?
        # This behavior is not consistent with the documentation
        resp = self.request(url="/itemresult/stats", content=params)
        if resp["success"] is True:
            itemstats = []
            for item in range(len(resp["itemresults"])):
                r = resp["itemresults"][item]
                r.update({"api_call_params": params})
                itemstats.append(RemindoStats(r))
            return itemstats
