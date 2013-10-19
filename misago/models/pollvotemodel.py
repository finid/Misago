from django.db import models

class PollVote(models.Model):
    poll = models.ForeignKey('Poll', related_name="vote_set")
    forum = models.ForeignKey('Forum')
    thread = models.ForeignKey('Thread')
    option = models.ForeignKey('PollOption', null=True, blank=True)
    user = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_slug = models.SlugField(max_length=255, null=True, blank=True)
    date = models.DateTimeField()
    ip = models.GenericIPAddressField()
    agent = models.CharField(max_length=255)

    class Meta:
        app_label = 'misago'