import json

from scrapy import Request, Spider


class MostFundedSpider(Spider):
    name = "most_funded"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))

    def start_requests(self):
        for i in range(1, self.pages + 1):
            yield Request(
                f"https://www.kickstarter.com/discover/advanced?sort=most_funded&page={i}"
            )

    def parse(self, response):
        projects = [
            json.loads(project)
            for project in response.css(
                'div.js-react-proj-card::attr("data-project")'
            ).getall()
        ]
        for project in projects:
            base_data = self.get_base_data(project)
            creator = self.get_creator(project)
            location = self.get_location(project)
            category = self.get_category(project)
            profile = self.get_profile(project)
            yield base_data | creator | location | category | profile

    def get_base_data(self, project):
        return {
            "id": project["id"],
            "name": project["name"],
            "blurb": project["blurb"],
            "goal": project["goal"],
            "pledged": project["pledged"],
            "percent_funded": project["percent_funded"],
            "state": project["state"],
            "country": project["country"],
            "currency": project["currency"],
            "deadline": project["deadline"],
            "state_changed_at": project["state_changed_at"],
            "created_at": project["created_at"],
            "launched_at": project["launched_at"],
            "staff_pick": project["staff_pick"],
            "backers_count": project["backers_count"],
            "static_usd_rate": project["static_usd_rate"],
            "usd_pledged": project["usd_pledged"],
            "converted_pledged_amount": project["converted_pledged_amount"],
            "fx_rate": project["fx_rate"],
            "usd_exchange_rate": project["usd_exchange_rate"],
            "usd_type": project["usd_type"],
            "spotlight": project["spotlight"],
            "project_url": project["urls"]["web"]["project"],
        }

    def get_creator(self, project):
        return {
            "creator_id": project["creator"]["id"],
            "creator_name": project["creator"]["name"],
            "creator_url": project["creator"]["urls"]["web"]["user"],
        }

    def get_location(self, project):
        return {
            "location_id": project["location"]["id"],
            "location_name": project["location"]["name"],
            "location_country": project["location"]["country"],
            "location_state": project["location"]["state"],
            "location_type": project["location"]["type"],
        }

    def get_category(self, project):
        return {
            "category_id": project["category"]["id"],
            "category_name": project["category"]["name"],
            "category_parent_id": project["category"].get("parent_id", None),
            "category_parent_name": project["category"].get("parent_name", None),
            "category_url": project["category"]["urls"]["web"]["discover"],
        }

    def get_profile(self, project):
        return {
            "profile_id": project["profile"]["id"],
            "profile_project_id": project["profile"]["project_id"],
            "profile_state": project["profile"]["state"],
            "profile_state_changed_at": project["profile"]["state_changed_at"],
            "profile_name": project["profile"]["name"],
            "profile_blurb": project["profile"]["blurb"],
        }
