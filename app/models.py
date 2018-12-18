from django.db import models

# Create your models here.
class Music(models.Model):
    song = models.TextField(max_length=300, help_text="歌曲", verbose_name="歌曲")
    singer = models.CharField(max_length=100, help_text="歌手", verbose_name="歌手")
    last_modify_date = models.DateTimeField(auto_now=True, verbose_name="最后修改时间", help_text="最后修改日期")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期",help_text="创建日期")

    class Meta:
        db_table = "music"
        verbose_name = "音乐"
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.song
