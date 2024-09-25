import os
from django.core.management.base import BaseCommand
from jobs.models import UserProfile
from dotenv import load_dotenv
from auto_jobs_applier import AutoJobsApplier

load_dotenv()


class Command(BaseCommand):
    help = "Runs the auto_jobs_applier for all users in the database"

    def handle(self, *args, **options):
        users = UserProfile.objects.all()

        for user in users:
            self.stdout.write(
                f"Running auto_jobs_applier for user: {user.user.username}"
            )

            applier = AutoJobsApplier(
                linkedin_email=user.linkedin_email,
                linkedin_password=user.linkedin_password,
                job_titles=user.job_titles.split(","),
                locations=user.locations.split(","),
                experience_level=user.experience_level,
                job_types=user.job_types.split(","),
                remote=user.remote,
                easy_apply=user.easy_apply,
                keywords=user.keywords.split(",") if user.keywords else None,
                openai_api_key=os.getenv("OPENAI_API_KEY"),
                linkedin_api_key=os.getenv("LINKEDIN_API_KEY"),
            )

            try:
                applier.run()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully ran auto_jobs_applier for user: {user.user.username}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error running auto_jobs_applier for user: {user.user.username}. Error: {str(e)}"
                    )
                )
