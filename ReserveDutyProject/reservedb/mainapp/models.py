from django.db import models

class Person(models.Model):

    ranks = [
        (1, 'סגן'),
        (2, 'סרן'),
        (3, 'רסן'),
        (4, 'סא"ל'),
        (5, 'אל"מ'),
        (6, 'סמ"ר'),
        (7, 'רס"ל'),
        (8, 'רס"ר'),
        (9, 'רס"מ'),
        (10, 'רס"ב'),
        (11, 'רנ"ג')
    ]
    groups = [
        (1, 'ביצועים'),
        (2, 'בקרת תצורה'),
        (3, 'תחום מט"ס'),
        (4, 'התעייפות'),
        (5, 'אל-הרס'),
        (6, 'טכנולוגיות')
    ]

    name = models.CharField(max_length=50, verbose_name='שם')
    rank = models.IntegerField(choices=ranks, verbose_name='דרגה')
    group = models.IntegerField(choices=groups, verbose_name='מדור')
    last_here = models.DateField(blank=True, null=True, verbose_name='תאריך אחרון')

    def __str__(self):
        return str(self.name)