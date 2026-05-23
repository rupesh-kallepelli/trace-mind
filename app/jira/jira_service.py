from jira import JIRA
from app.core.config import settings

jira_client = JIRA(
    server=settings.JIRA_URL,
    basic_auth=(
        settings.JIRA_USERNAME,
        settings.JIRA_API_TOKEN
    )
)

class JiraService:

    @staticmethod
    def fetch_incidents():

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