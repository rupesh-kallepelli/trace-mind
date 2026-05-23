from jira import JIRA
from app.core.config import settings

jira_client = None

if settings.JIRA_ENABLED:
    try:

        jira_client = JIRA(
            server=settings.JIRA_URL,
            basic_auth=(
                settings.JIRA_USERNAME,
                settings.JIRA_API_TOKEN
            )
        )

        jira_client.server_info()

        print("JIRA integration initialized")

    except Exception as ex:
        print(f"JIRA unavailable: {ex}")
        jira_client = None


class JiraService:

    @staticmethod
    def fetch_incidents():

        ##################################################################
        # JIRA DISABLED / UNAVAILABLE
        ##################################################################

        if not jira_client:
            return []

        try:

            issues = jira_client.search_issues(
                'project = PROD ORDER BY created DESC',
                maxResults=10
            )

            return [
                {
                    "id": issue.key,
                    "summary": issue.fields.summary
                }
                for issue in issues
            ]

        except Exception as ex:

            print(f"Failed fetching JIRA incidents: {ex}")

            return []