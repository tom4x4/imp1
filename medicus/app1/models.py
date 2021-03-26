from django.db import models

class Bloz(models.Model):
    kod07 = models.CharField('Bloz', max_length=7, primary_key=True)
    nazwa = models.CharField('Nazwa', max_length=100)
    dawka = models.CharField('Dawka', max_length=50,null=True,blank=True)
    opakh = models.CharField('Opakowanie', max_length=40,null=True,blank=True)
    prodc = models.CharField('Producent', max_length=60,null=True,blank=True)
    kodkr = models.CharField('EAN', max_length=14,null=True,blank=True)
    class Meta:
        managed = False
        db_table = 'BLOZ'
        indexes = [
            models.Index(fields=['kod07',]),
            models.Index(fields=['nazwa','-nazwa']),
            models.Index(fields=['kodkr',]),
            models.Index(fields=['prodc', ])
                     ]

class Apteki(models.Model):
    id = models.AutoField(primary_key=True)
    apteka = models.CharField('Apteka',max_length=14)
    ip = models.GenericIPAddressField('Ip', protocol='IPv4')
    def __str__(self):
        # zwraca kolumny w admin
        return ("{}  {}" .format(self.apteka,self.ip ))
    class Meta:
        verbose_name = 'Apteki'
        # verbose_name_plural ='xxxx'







