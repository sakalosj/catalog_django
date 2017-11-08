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
    # material = models.CharField(max_length=45)
    materialList =  models.ForeignKey('MaterialList', on_delete=models.CASCADE, null=True)

    research= models.ManyToManyField(
        'Research',
        through='ResearchRelation',
        # through_fields=('object', 'project', 'research'),
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)

class ResearchRelation(models.Model):
    project = models.ForeignKey('Project', on_delete= models.CASCADE)

    object = models.ForeignKey(Object, on_delete= models.PROTECT)
    research = models.ForeignKey('Research', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    garant = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    realized_by = models.CharField(max_length=45)
    realized_for = models.CharField(max_length=45)
    restorers = models.ManyToManyField(Restorer)
    objects = models.ManyToManyField(Object)

class Material(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200) #general info

class MaterialList(models.Model):
    name = models.CharField(max_length=45)
    materials =  models.ManyToManyField(
        Material,
        through='Material2MaterialList',
        # through_fields=('materialList', 'material'),
    )


class Material2MaterialList(models.Model):
    material = models.ForeignKey(Material, on_delete= models.PROTECT)
    materialList = models.ForeignKey(MaterialList, on_delete= models.CASCADE)
    description = models.CharField(max_length=200) #project specific info


class Research(models.Model):
    UVA = models.BooleanField()
    UVC = models.BooleanField()
    RUVA = models.BooleanField()
    IR = models.BooleanField()
    RTG = models.BooleanField()
    CT = models.BooleanField()
    ch_t_research = models.BooleanField()
    sondazny = models.CharField(max_length=200)
    other = models.CharField(max_length=200)



