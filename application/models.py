from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def profile_image(instance, filename):
    """
    This function generates the path where a profile image should be saved to.
    :param instance: Instance of Member to be saved
    :param filename: Name of file to be uploaded
    :return: Path of file
    """
    ext = filename.split('.')[-1]
    return 'image/user_{0}.{1}'.format(instance.user.id, ext)


class Team(models.Model):
    """
    This represents a Team object in our database. Each team has a team lead
    and a deputy team lead.
    """
    name = models.CharField(max_length=30)
    lead = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='team_lead', null=True, blank=True)
    deputy = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='deputy_team_lead', null=True,
                               blank=True)

    def __str__(self):
        return self.name


class Objective(models.Model):
    """
    This represents an objective of Africa Literary Project in our database.
    """
    description = models.TextField()

    def __str__(self):
        return self.description


class Member(models.Model):
    """
    This represents a member account in our database. When a member is
    created their approval defaults to False until they are approved by HR.
    """
    GENDER = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    IS_EXPERIENCED_WRITER = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ('M', 'Maybe')
    ]
    THOUGHTS_ON_WRITING_SPACE = [
        ('SA', 'Strongly Agree'),
        ('A', 'Agree'),
        ('N', 'Neutral'),
        ('D', 'Disagree'),
        ('SD', 'Strongly Disagree')
    ]
    CAN_DONATE_FOR_BOOKDRIVE = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    about = models.TextField()
    telephone = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to=profile_image)
    gender = models.CharField(choices=GENDER, max_length=30)
    address = models.TextField()
    fav_color = models.CharField(max_length=30)
    objectives = models.ManyToManyField(Objective)
    teams = models.ManyToManyField(Team)
    idea_promote_reading = models.TextField(null=True)
    idea_project_successful = models.TextField(null=True)
    idea_achieve_objectives = models.TextField(null=True)
    is_experienced_writer = models.CharField(max_length=10, null=True,
                                             choices=IS_EXPERIENCED_WRITER)
    idea_funding = models.TextField(null=True)
    can_donate_for_bookdrive = models.CharField(max_length=10, null=True,
                                                choices=CAN_DONATE_FOR_BOOKDRIVE)
    thoughts_on_writing_space = models.CharField(max_length=20, null=True,
                                                 choices=THOUGHTS_ON_WRITING_SPACE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()
