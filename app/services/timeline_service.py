from datetime import datetime

class TimelineService:

    @staticmethod
    def reconstruct(logs):

        return [
            {
                "timestamp": str(datetime.utcnow()),
                "event": log
            }
            for log in logs
        ]