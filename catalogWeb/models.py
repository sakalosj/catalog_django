from django.db import models

# Create your models here.


class Restorer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Monument(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    date = models.DateField()
    provenance = models.CharField(max_length=45)
    dimensions = models.CharField(max_length=45)
    technique = models.CharField(max_length=45)
    # picture_list_id_fk = models.CharField(max_length=45)
    # material = models.CharField(max_length=45)
    materialList =  models.OneToOneField('MaterialList', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)


class Monument2Project(models.Model):
    monument = models.ForeignKey(Monument,on_delete=models.CASCADE)
    project = models.ForeignKey('Project',on_delete=models.CASCADE)
    testfield = models.CharField(max_length=45)


class ResearchRelation(models.Model):
    project = models.ForeignKey('Project', on_delete= models.CASCADE,blank=True,null=True)
    monument = models.ForeignKey(Monument, on_delete= models.PROTECT,blank=True,null=True)
    research = models.ForeignKey('Research', on_delete=models.CASCADE,blank=True,null=True)
    description = models.CharField(max_length=200)


class Project(models.Model):
    name = models.CharField(max_length=45)
    garant = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    realized_by = models.CharField(max_length=45)
    realized_for = models.CharField(max_length=45)
    restorerList = models.ManyToManyField(Restorer,blank=True)
    monumentList = models.ManyToManyField(Monument,blank=True,through=Monument2Project)
    researchList = models.ManyToManyField('Research',blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)


class Material(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200) #general info

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)


class MaterialList(models.Model):
    name = models.CharField(max_length=45)
    materials =  models.ManyToManyField(
        Material,
        through='Material2MaterialList',
        # through_fields=('materialList', 'material'),
        blank=True
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)


class Material2MaterialList(models.Model):
    material = models.ForeignKey(Material, on_delete= models.PROTECT)
    materialList = models.ForeignKey(MaterialList, on_delete= models.CASCADE)
    description = models.CharField(max_length=200) #project specific info



class Research(models.Model):
    name = models.CharField(max_length=45)
    # monumentList = models.ForeignKey(Monument,blank=True,null=True,on_delete=models.SET_NULL)
    projectRelation = models.OneToOneField(Monument2Project, on_delete=models.CASCADE)
    monument2ProjectRelation = models.ForeignKey(Project,blank=True,null=True,on_delete=models.CASCADE)
    UVA = models.BooleanField()
    UVC = models.BooleanField()
    RUVA = models.BooleanField()
    IR = models.BooleanField()
    RTG = models.BooleanField()
    CT = models.BooleanField()
    ch_t_research = models.BooleanField()
    sondazny = models.CharField(max_length=200)
    other = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)





