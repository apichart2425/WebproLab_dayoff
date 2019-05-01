from django.db import models

# Create your models here.
class Dayoff(models.Model):
    create_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    reason = models.TextField()
    TYPE_Frist = 'ลากิจ'
    TYPE_Second ='ลาป่วย'
    TYPES = (
        (TYPE_Frist ,'ลากิจ'),
        (TYPE_Second ,'ลาป่วย')
    )
    type = models.CharField(max_length=50, choices=TYPES, default='01', null=False)
    date_start = models.DateField()
    date_end = models.DateField()

    Status_one = 'รอการอนุมัติ'
    Status_two = 'ไม่อนุมัติ'
    Status_tree = 'อนุมัติ'
    Status = (
        (Status_one, 'รอการอนุมัติ'),
        (Status_two, 'ไม่อนุมัติ'),
        (Status_tree, 'อนุมัติ')
    )
    approve_status = models.CharField(max_length=50, choices=Status, default='รอการอนุมัติ', null=False)
