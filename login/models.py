from django.db import models



class UserProfile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_user_by_username(username):
        try:
            return UserProfile.objects.get(username=username)
        except:
            return False


    def isExists(self):
        if UserProfile.objects.filter(username = self.username):
            return True
        return False

    def register(self):
        self.save()


    def __str__(self):
        return f"{self.first_name}"


