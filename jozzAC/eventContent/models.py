from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
def update_filename(instance, filename):
	ext 	= filename.split('.')[-1]
	filename 	= "%s.%s" % (instance.nama_Content, ext)
	return filename

def upload_location(instance, filename, **kwargs):
	path = update_filename(instance, filename)
	file_path = 'eventContent/{path}'.format(path=path)
	return file_path

class eventContentModel(models.Model):

   admin                     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
   nama_Content			     = models.CharField(max_length=50)
   images_Content 			  = models.ImageField(upload_to=upload_location, null=False, blank=True)
   keterangan_Content		  = models.TextField()
   tgl_upload                = models.DateField(auto_now=True)
   slug_Content			     = models.SlugField()

   class Meta:
      verbose_name='Event'

   def save(self):
      self.slug_Content	= slugify(f"{self.nama_Content}")
      super().save()

   def __str__(self):
      return f"{self.nama_Content}"


@receiver(post_delete, sender=eventContentModel)
def submission_delete(sender, instance, **kwargs):
	instance.images_Content.delete(False)


