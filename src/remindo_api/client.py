# src/remindo_api/client.py
"""Client for Remindo."""
from typing import Any, List

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


# TODO: complete list_subscritpion call
# TODO: complete mypy typing


class RemindoClientException(Exception):
    """Class that is called for exception messages.

    You can see the usage of this class looking at the test.
    """

    def __init__(self, error_msg):
        """Init exception."""
        self.error_msg = error_msg

    def __str__(self):
        """Return exception."""
        return self.error_msg


class RemindoClient:
    """Main client class of Remindo."""

    def __init__(self, uuid, secret, url_base, sha = "SHA512") -> None:
        """Initialize a RemindoClient.

        It uses parameters that one needs to obtain from Paragin.

        Args:
            uuid (str): uuid of the account with access to Remindo.
            secret (str): secret of the account with access to
                Remindo.
            url_base (str) : url_base for accessing Remindo.
                Changes depending on each university and between
                test and production environemnts.

        """
        self.uuid = uuid
        self.secret = secret
        self.url_base = url_base
        self.sha = sha
        self.ip = requests.get("https://jsonip.com").json()["ip"]
        """str: current ip from which Remindo is accessed.
            It needs to be authorized.
        """

    @property
    def query_dict(self) -> dict:
        """Query personal data from client."""
        return {"key": self.uuid, "secret": self.secret, "url_base": self.url_base, "sha": self.sha}

    def request(self, *args, **kwargs):
        """Create a remindo_api object and make a request."""
        req = RemindoRequest(self, *args, **kwargs)
        return req.request()

    def hello_world(self) -> RemindoRequest:
        """Make a "Hello World" request to verify key and connection.

        Returns:
            :obj:`RemindoHelloWorld`: Object RemindoHelloWorld. Contains string "hello world" if
                successfull, none if not.
        """
        resp = self.request(url="/remote_api/hello_world", content="")
        return RemindoHelloWorld(resp)

    def list_clusters(
        self, filter: str = None, category: str = None, full: bool = True
    ) -> List[RemindoCluster]:
        """List all available user groups.

        Args:
            filter (str): A search query for the name of the cluster.
            category (str): Return only user groups in this category.
            full (bool): Return all the user groups.

        Returns:
            :obj:`dict` of :obj:`RemindoCluster`: A list of dict of user groups in the form:
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
        self,
        code: str = None,
        study_id: int = None,
        datasource_uuid: str = None,
        complete: bool = False,
        since: str = None,
    ) -> list:
        """List studies.

        Studies are a set of recipes.

        Args:
            code (str): Return studies with study code
            study_id (int): Optional; Return study with ID
            datasource_uuid (str): Optional; Return studies from test manager with UUID
            complete (bool): Optional; Full study & all recipes)
            since (str): Optional; Date is in Y-m-d format. To be filled only when complete is true

        Returns:
            :obj:`list` of :obj:`RemindoStudy`: Return list of Remindo studies
            :obj:`list` of :obj:`RemindoRecipe`: if complete == True, return list of studies and associated recipes modified since date

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
        code: str = None,
        category: str = None,
        study_id: int = None,
        recipe_id: int = None,
        filtr: str = None,
        datasource_uuid: str = None,
        since: str = None,
        properties: bool = None,
        full: bool = False,
    ) -> List[RemindoRecipe]:
        """List recipes.

        Recipe is a list of question for a determined exam - needs to be assigned
        to a student with a 'subscription' before starting exam.

        Args:
            code (str): When given, it will only return recipes where the recipe code contains the given text.
            category (str): When given, it will only return recipes where the recipe category contains the given text.
            study_id (int): When given, only the recipes in the study with this ID are returned.
            recipe_id (int): When given, only the recipe with the given ID is returned
            filtr (str): Optional; Search query for retrieving the recipe
            datasource_uuid (str): Optional; Return recipes from test manager with UUID
            since (str): Optional; Return recipes modified since
            properties (bool): Optional; Returns the custom from test manager
            full (bool): Optional; Returns additional information

        Returns:
            :obj:`list` of :obj:`RemindoRecipe`: Return list of Remindo recipe object(s)
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

    def list_moments(
        self,
        ids: int = None,
        code: str = None,
        recipe_ids: int = None,
        frm: str = None,
        until: str = None,
    ) -> List[RemindoMoment]:
        """List moments.

        Args:
            ids (int): Return moment for test id(s)
            code (str): Return list for test moment code(s)
            recipe_ids (int): Optional; Return moments with recipe id(s)
            frm (str): Optional; Return moments after date
            until (str): Optional; Return moments before date

        Returns:
            :obj:`list` of :obj:`RemindoMoment`: Return list of RemindoMoment object(s)
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
        id: int = None,
        code: int = None,
        candidate_ids: int = None,
        candidate_codes: int = None,
        candidate_filter: str = None,
    ) -> List[RemindoResult]:
        """List results of selected moments.

        Args:
            id (int): ID of moment
            code (int): Code of moment
            candidate_ids (int): Optional; Return result for candidate id
            candidate_codes (int): Optional; Return result for candidate code(s)
            candidate_filter (str): Optional; Filter object to retrieve user

        Returns:
            :obj:`list` of :obj:`RemindoResult`: Return list of Remindo Result object(s) for the moment.
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
        typ: str = None,
        modified_since: str = None,
        modified_until: str = None,
        start_time_since: str = None,
        start_time_until: str = None,
        end_time_since: str = None,
        end_time_until: str = None,
        status: str = None,
        search: str = None,
        candidate_ids: int = None,
        cluster_ids: int = None,
        study_ids: int = None,
        recipe_ids: int = None,
        result_ids: int = None,
        subscription_ids: int = None,
        page: int = None,
        page_size: int = None,
        complete: bool = False,
    ) -> List[RemindoResult]:
        """Retrieve list of results.

        Args:
            typ (str): Optional; Restrict by type: practice, graded practice, exam
            modified_since (str): Optional; Restrict by date and time of last modification
            modified_until (str): Optional; Restrict by date and time of last modification
            start_time_since (str): Optional; Restrict by date and time of start
            start_time_until (str): Optional; Restrict by date and time of start
            end_time_since (str): Optional; Restrict by date and time of end
            end_time_until (str): Optional; Restrict by date and time of end
            status (str): Optional; Restrict by results with status: started, finished, review, closed
            search (str): Optional; Restrict by recipe name or user name match
            candidate_ids (int): Optional; Restrict by candidates IDs
            cluster_ids (int): Optional; Restrict by clusters IDs
            study_ids (int): Optional; Restrict by studies IDs
            recipe_ids (int): Optional; Restrict by recipes IDs
            result_ids (int): Optional; Restrict by results IDs
            subscription_ids (int): Optional; Restrict by subscriptions IDs
            page (int): Optional; Page to be requested, starting at 1
            page_size (int): Optional; Desirable page size, from 1 to 200
            complete (bool): Optional; Adds fields report_data and actionlog

        Returns:
            :obj:`list` of :obj:`RemindoResult`:
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
        recipe_id: int = None,
        moment_id: int = None,
        subscription_ids: int = None,
        user_ids: int = None,
        add_item_info: bool = False,
    ) -> Any:
        """List subscription results.

        No more than 50.000.

        Args:
            recipe_id (int): Recipe ID to retrive item result statistics.
            moment_id (int): Optional; Limit results to this moment.
            subscription_ids (int): Optional; Limit results to this subscription ID.
            user_ids (int): Optional; Limit results to user IDs.
            add_item_info (bool): Optional; If true, and with single subscription_id or single user_id,
                add extra information for each item

        Returns:
            :obj:`list` of :obj:`RemindoResult`: Returns results tied to subscription.
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
        recipe_id: int = None,
        moment_id: int = None,
        variant_id: int = None,
        scan_id: int = None,
        corrections: list = None,
        locale: str = None,
    ) -> Any:
        """Calculate result reliability.

        Calculate the reliability over a set of results using cronbach’s alpha
        and the standard error of measurement.You always need to filter on a single
        recipe to calculate the reliability. Either using a test moment, a recipe,
        a scan or a paper variant.

        Args:
            recipe_id (int): Optional; Calculate reliability for the given test recipe
            moment_id (int): Calculate reliability for the given test moment
            variant_id (int): Optional; Calculate reliability for the given paper variant
            scan_id (int): Optional; Calculate reliability for the given scan corrections
            corrections (list): Optional; Which answer model corrections to apply while calculating the reliability.
                Available are: `active` (active corrections) or `concept` (concept corrections)
            locale (str): Optional; The language in which to provide extra information (notes)

        Returns:
            :obj:`RemindoReliability`: Returns object containing reliability parameters.
        """

        params = {}
        if recipe_id is not None:
            params["recipe_id"] = recipe_id
        if moment_id is not None:
            params["moment_id"] = moment_id
        if variant_id is not None:
            params["variant_id"] = variant_id
        if corrections is not None:
            params["corrections"] = corrections
        if locale is not None:
            params["locale"] = locale

        resp = self.request(url="/result/reliability", content=params)
        resp.update({"api_call_params": params})
        return RemindoReliability(resp)

    def list_item_results(
        self,
        recipe_id: int = None,
        moment_id: int = None,
        subscription_ids: int = None,
        user_ids: int = None,
        add_item_info: bool = False,
    ) -> List[RemindoItem]:
        """Retrieve item results.

        Returns a list of question/item results for a given filter. No more than 50.000
        item results will be returned. The result is a nested array, grouped by subscription
        id and test section (if applicable).

        Args:
            recipe_id (int): The recipe ID for which you want to retrieve the item result statistic
            moment_id (int): Limit the item results to the ones used in this moment
            subscription_ids (int): Optional; Limit the item results to the given subscription IDs
            user_ids (int): Optional; Limit the item results to the given user IDs
            add_item_info (bool): Optional; If true, and in combination with a single subscription_id or a single user_id,
                will add extra information for each item, such as item properties, the author
                of the item and the time it was created

        Returns:
            :obj:`list` of :obj:`RemindoItem`: Returns list of RemindoItem containing the results for each item (question) on the test.
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
                count_items = 0
                for s in range(sections):
                    # section = resp[subscription][s]["section"]
                    # section_id = resp[subscription][s]["section_id"]
                    items = resp[subscription][s]["itemresults"].keys()
                    for i in items:
                        count_items += 1
                        it = resp[subscription][s]["itemresults"][i]
                        it.update(
                            {
                                "subscription_id": subscription,
                                "position_item": count_items,
                                "api_call_params": params,
                            }
                        )
                        itemresults.append(RemindoItem(it))
            return itemresults
        else:
            return None

    def list_stats(
        self,
        recipe_id: int = None,
        moment_id: int = None,
        subscription_ids: int = None,
        user_ids: int = None,
    ) -> List[RemindoStats]:
        """Retrieve recipe question/item result statistics.

        Returns a list of aggregated statistics for each question/item results for a given
        recipe of pair recipe-moment.

        Args:
            recipe_id (int): The recipe ID for which you want to retrieve the item result statistics
            moment_id (int): Optional; Limit the item results to the ones used in this moment.
            subscription_ids (int): Optional; Limit the item results to the given subscription IDs
            user_ids (int): Optional; Limit the item results to the given user IDs

        Returns:
            :obj:`list` of :obj:`RemindoStat`: Returns list of RemindoStat for each of the items (questions) on the exam.
                Each stat contains the summarized values for one question.
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
