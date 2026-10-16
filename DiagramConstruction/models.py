from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30)
    hash = models.CharField(max_length=256)

    def __str__(self):
        return self.login


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)
    end_date = models.DateField()

    def __str__(self):
            return f'Session of {self.user}'


class Theme(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)


class Mistake(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)


class ServerMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1000)
    expected_response = models.CharField(max_length=1000)
    themes = models.ManyToManyField(Theme)
    message_date = models.DateField(auto_now_add=True)


class UserMessage(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    server_message = models.OneToOneField(ServerMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=1000)
    message_length = models.IntegerField()
    message_date = models.DateField(auto_now_add=True)
    correct = models.BooleanField(default=False)


class UserMistake(models.Model):
    user_message = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    mistake = models.ForeignKey(Mistake, on_delete=models.CASCADE)