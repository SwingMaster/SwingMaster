from django.db import models

class UserScore(models.Model):
    userscore_name = models.ForeignKey("signup.User", related_name="u_name", on_delete=models.CASCADE, db_column='userscore_name')
    userscore_id = models.CharField(max_length=32, verbose_name="유저 아이디")
    userscore_nickname = models.CharField(max_length=32, verbose_name="유저 닉네임")
    userscore_score = models.IntegerField(default=30, verbose_name="유저 점수")
    userscore_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='점수 생성시간')

    def __str__(self):
        return self.userscore_nickname

    class Meta:
        db_table = "userscore"
        verbose_name = "유저 점수"
        verbose_name_plural = "유저 점수"
