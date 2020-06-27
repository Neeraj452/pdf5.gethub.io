from django.db import models

# Create your models here.
class My_pdf(models.Model):
    semester = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default="")
    pdf = models.FileField(upload_to='books/pdfs/')
    image = models.ImageField(upload_to='books/image/',null=True,blank=True)


    def __str__(self):
        return self.subject
    def delete(self,*args, **kwargs):
        self.pdf.delete()
        self.image.delete()
        super().delete(*args, **kwargs)





















































