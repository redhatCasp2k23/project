from django.db import models
from account.models import UserExtra


class Report(models.Model):
    user = models.ForeignKey(
        to=UserExtra,
        on_delete=models.SET_NULL,
        null=True
    )
    issue_title = models.CharField(
        verbose_name="issue_title",
        null=True,
        blank=True,
        max_length=100
    )
    location = models.CharField(
        verbose_name="issue_location",
        max_length=1000,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )
    report_date = models.DateTimeField(auto_now_add=True)
    issue_status = models.CharField(
        verbose_name="issue_status",
        choices=(
        ('0','pending'),
        ('1','solved'),
        ('2','closeCase'),
        ('3','rejected')
        ),
        default='0'
        ,
        max_length=1
    )
    issue_image = models.ImageField(
        max_length=300,
        upload_to="Issue image"
    )
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.issue_title


class Vote(models.Model):
    user = models.ForeignKey(
        to=UserExtra,
        on_delete=models.CASCADE
    )
    report = models.ForeignKey(
        to=Report,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'report')

    def update_vote_count(self):
        self.report.vote_count += 1
        self.report.save()

class SolvedImage(models.Model):
    report = models.ForeignKey(
        to=Report,
        on_delete=models.CASCADE
    )
    solved_image = models.ImageField(
        max_length=300,
        upload_to='solve image',
        null=True
    )

    def __str__(self):
        return self.report.issue_title

    class Meta:
        unique_together = ('solved_image', 'report')

