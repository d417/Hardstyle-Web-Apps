from django.db import models
import datetime

class Item(models.Model):
    
    MON_CHOICES = (
        ('1月', '1月'),
        ('2月', '2月'),
        ('3月', '3月'),
        ('4月', '4月'),
        ('5月', '5月'),
        ('6月', '6月'),
        ('7月', '7月'),
        ('8月', '8月'),
        ('9月', '9月'),
        ('10月', '10月'),
        ('11月', '11月'),
        ('12月', '12月'),
    )
    month = datetime.date.today().month
    mon = models.CharField(
        verbose_name='提出月',
        choices=MON_CHOICES,
        default=month,
        max_length=3,
    )

    name = models.CharField(
        verbose_name='氏名',
        max_length=200,
    )

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
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return str(self.mon) + '_' + str(self.name) + 'のレポート'

    class Meta:
        verbose_name = 'レポート'
        verbose_name_plural = 'レポート'
