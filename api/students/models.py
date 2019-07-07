from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from accounts.models import Timestamp


class Branch(Timestamp):
    name = models.CharField(max_length=64)
    hod = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return slugify(self.name)


class Student(Timestamp):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNSPECIFIED = 'UNSPECIFIED'
    GENDER_CHOICES = (
        (MALE,'Male'),
        (FEMALE,'Female'),
        (UNSPECIFIED,'Unspecified')
    )
    GEN = 'GEN'
    OBC = 'OBC'
    SC = 'SC'
    ST = 'ST'
    CATEGORY_CHOICES = (
        (GEN,'Gen'),
        (OBC,'OBC'),
        (ST,'ST'),
        (SC,'SC')
    )
    MODE_OF_ADMISSION = (
        ('vacant_seat', 'Vacant Seat'),
        ('upsee', 'UPSEE'),
    )
    MODE_OF_ADMISSION_CATEGORY = (
        ('Lateral_entry', 'Lateral Entry'),
        ('FW', 'FW'),
        ('EWS', 'EWS'),
        ('other', 'other')
    )
    roll_no = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=64)
    father_name = models.CharField(max_length=64)
    mother_name = models.CharField(max_length=64)
    dob = models.DateField()
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES)
    category = models.CharField(max_length=16, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=16)
    address = models.TextField()
    mobile_no = models.CharField(max_length=10)
    father_mobile_no = models.CharField(max_length=10)
    mother_mobile_no = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    addhar_no = models.CharField(max_length=16, unique=True)
    mode_of_admission = models.CharField(max_length=16, choices=MODE_OF_ADMISSION)
    mode_of_admission_category = models.CharField(max_length=16, choices=MODE_OF_ADMISSION_CATEGORY)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no