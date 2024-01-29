from django.db import transaction
from ..models import JobModel


class JobsHandler:
    def __init__(self):
        pass

    async def fetch_certain_job(self, job_id: int):
        try:

            return await JobModel.objects.filter()

        except Exception as e:
            pass

    def fetch_all_jobs(self):
        try:
           return JobModel.objects.all()
        except Exception as e:
            print("error ", str(e))
            pass
