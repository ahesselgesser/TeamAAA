from django.db import models


class Report(models.Model):
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
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/%Y%m%d-{0}'.format(filename)

class FileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)   
