from django.db import models

# Create your models here.


class Restorer(models.Model):
    restorer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Object(models.Model):
    object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    date = models.DateField()
    provenance = models.CharField(max_length=45)
    dimensions = models.CharField(max_length=45)
    technique = models.CharField(max_length=45)
    # picture_list_id_fk = models.CharField(max_length=45)
    # material_list_id_fk = models.CharField(max_length=45)
    # research_id_fk = models.CharField(max_length=45)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    garant = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    realized_by = models.CharField(max_length=45)
    realized_for = models.CharField(max_length=45)
    restorers = models.ManyToManyField(Restorer)
    objects = models.ManyToManyField(Object)