from django.db import models

class Icon(models.Model):

    img         = models.ImageField(verbose_name="アイコン",upload_to="icon/")
    name        = models.CharField(verbose_name="アイコンの名前",max_length=20)

    def __str__(self):
        return self.name

class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    lat         = models.DecimalField(verbose_name="緯度",max_digits=9, decimal_places=6)
    lon         = models.DecimalField(verbose_name="経度",max_digits=9, decimal_places=6)
    icon        = models.ForeignKey(Icon,verbose_name="アイコン",on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
