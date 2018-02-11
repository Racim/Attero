from django.db import models
#from treebeard.mp_tree import MP_Node
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.

class ReportTemplate(models.Model):
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='report_templates/')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed')
    )

    title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    report_template = models.ForeignKey(ReportTemplate, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = (
            ('view_project', 'Can view Project'),
        )


class Note(MPTTModel):
    title = models.CharField(max_length=255)
    note = models.TextField()
    report = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


class Task(MPTTModel):
    name = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']



class NoteTemplate(MPTTModel):
    title = models.CharField(max_length=255)
    note = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']



