from django.db import models
from django.utils import timezone


class Item(models.Model):

    name = models.CharField(
        verbose_name='氏名',
        max_length=200,
    )

    locale = models.CharField(
        verbose_name='顧客名/作業場所',
        max_length=200,
    )

    projectstatus = models.TextField(
        verbose_name='案件状況',
        max_length=300,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '月報'
        verbose_name_plural = '月報'
