"""
Includes most common models used extensively by all users across the site
Copied from previous project with some modifications
"""
from django.db import models
from django.contrib.auth.models import User

class NonArchivedManager(models.Manager):
    """
    Includes only active objects
    """
    def get_queryset(self):
        """
        Retrieves only active objects within type

        Returns:
            QuerySet : active objects only
        """
        return super().get_queryset().filter(active=True)
"""
Made for current project; model for uploading reports to site
"""
class UploadReport(models.Model):
    title = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='reports/pdfs/')
    cover = models.ImageField(upload_to='reports/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Report(models.Model):
    """
    Report model which collects attributes specific to a report and completion status
    """
    year = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    #degreeProgram = models.ForeignKey('DegreeProgram', on_delete=models.CASCADE, verbose_name="degree program")
    #Editied:
    degreeProgram = models.CharField(max_length=100, blank=True)
    #End of Edits
    accredited = models.BooleanField(default=False)
    date_range_of_reported_data = models.CharField(max_length=500,blank=True, null=True)
    #rubric = models.OneToOneField('GradedRubric', on_delete=models.SET_NULL, null=True)
    section1Comment = models.CharField(max_length=2000, blank=True, null=True, verbose_name="section I comment")
    section2Comment = models.CharField(max_length=2000, blank=True, null=True, verbose_name="section II comment")
    section3Comment = models.CharField(max_length=2000, blank=True, null=True, verbose_name="section III comment")
    section4Comment = models.CharField(max_length=2000, blank=True, null=True, verbose_name="section IV comment")
    submitted = models.BooleanField()
    returned = models.BooleanField(default=False)
    numberOfSLOs = models.PositiveIntegerField(default=0, verbose_name="number of SLOs")
    """
    Content added to report model for this project
    """
    title = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100)

class Profile(models.Model):
    """
    Model to hold extra information in addition to Django's User class, including whether they are 
    AAC members and the department
    """
    #first name, last name and email are included in the built-in User class. Access them through the user field
    aac = models.BooleanField(null=True)
    #False = faculty member/dept account
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

"""
Models added in newer project
"""
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/%Y%m%d-{0}'.format(filename)

class FileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)   
