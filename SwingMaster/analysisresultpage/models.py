from django.db import models

class UserScore(models.Model):
    userscore_id = models.CharField(max_length=32 ,verbose_name="유저 아이디", primary_key=True)
    userscore_nickname = models.ForeignKey("signup.User", related_name="u_nickname", on_delete=models.PROTECT, db_column='userscore_nickname')
    userscore_score = models.IntegerField(verbose_name="유저 점수")

    def __str__(self):
        return self.userscore_id

    class Meta:
        db_table = "userscore"
        verbose_name = "유저 점수"
        verbose_name_plural = "유저 점수"