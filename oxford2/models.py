from django.db import models

# These are the basic tables for Oxford 2.0:
# They are under the following categories:
#
# CATEGORIES - Define all the top-level categories for the nav menu
# PROJECTS - All the URLs, types, categories, etc for Jenkins builds
# NAVIGATION TREE ITEMS - Additional pages that aren't bound to a project
# VERSIONS - A linked table for all projects to list all doc version #s
# CONFIG - Admin configuration

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    display_name = models.CharField(max_length=100)
    weight = models.FloatField()
    def __str__(self):
        return self.display_name

class BuildType(models.Model):
    build_type = models.CharField(max_length=50)
    def __str__(self):
        return self.build_type

class ParserType(models.Model):
    parser_type = models.CharField(max_length=50)
    def __str__(self):
        return self.parser_type

class Project(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255)
    build_type = models.ForeignKey(BuildType, on_delete=models.CASCADE)
    parser = models.ForeignKey(ParserType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    artifact_url = models.CharField(max_length=255)
    weight = models.FloatField()
    visible = models.BooleanField()
    active = models.BooleanField()
    def __str__(self):
        return self.name

class NavTreeItem(models.Model):
    display_name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item_url = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.FloatField()
    visible = models.BooleanField()
    def __str__(self):
        return self.display_name

class Version(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    def __str__(self):
        return self.project

class Config(models.Model):
    polling_time = models.FloatField()
    max_versions = models.IntegerField()
    def __str__(self):
        return self.polling_time
    
