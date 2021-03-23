class FIRM(models.Model):
    id = models.IntegerField(primary_key=True)  # idfirm
    idnasz = models.CharField(max_length=3)
    nazwa = models.CharField(max_length=25)
    ilkzak = models.IntegerField(default=0, blank=True)
    iltowr = models.IntegerField(default=0, blank=True)
    lastup = models.DateTimeField(null=True, blank=True)


class TOWR(models.Model):
    id = models.BigIntegerField(primary_key=True)  # idfirm+idtowr
    idfirm = models.ForeignKey('FIRM', on_delete=models.CASCADE)
    idtowr = models.IntegerField()
    iddost = models.IntegerField()
    idklas = models.IntegerField()
    nazwa = models.CharField(max_length=42)
    nrtow = models.SmallIntegerField()
    wskus = models.SmallIntegerField()
    dgakt = models.DateTimeField()
    bloz7 = models.CharField(max_length=7, null=True)
    kodean = models.CharField(max_length=30, null=True)
    wertb = models.BigIntegerField()

    class Meta:
        unique_together = (('idfirm', 'idtowr'),)
        indexes = [
            models.Index(fields=['nazwat', ]),
            models.Index(fields=['nrtow', ]),
            models.Index(fields=['nazwa', '-nazwa']),
            models.Index(fields=['bloz7', ]),
            models.Index(fields=['wertb', ]),
        ]


class DOKF(models.Model):
    id = models.BigIntegerField(primary_key=True)  # idfirm+iddokf
    idfirm = models.ForeignKey('FIRM', on_delete=models.CASCADE)


class KZAK(models.Model):
    id = models.BigIntegerField(primary_key=True)  # idfirm+idkzak
    idfirm = models.ForeignKey('FIRM', on_delete=models.CASCADE)
    iddokf = models.ForeignKey('DOKF', on_delete=models.CASCADE)
    idkzak = models.IntegerField()
    idtowr = models.ForeignKey('TOWR', on_delete=models.CASCADE)
    ilakt = models.FloatField()
    empty = models.SmallIntegerField()
    wskus = models.SmallIntegerField()
    wstrz = models.SmallIntegerField()
    czfnt = models.FloatField()
    csabr = models.FloatField()
    datzk = models.DateTimeField()
    datwz = models.DateTimeField(null=True)
    datos = models.DateTimeField(null=True)
    dgakt = models.DateTimeField()
    kodkr = models.CharField(max_length=30, null=True)
    idzewn = models.BigIntegerField(null=True)
    seria = models.CharField(max_length=25, null=True)
    wertb = models.BigIntegerField()

    class Meta:
        unique_together = (('idfirm', 'idkzak'), ('idfirm', 'idtowr'), ('idfirm', 'iddokf'),
                           ('idfirm', 'idkzak', 'idtowr'), ('idfirm', 'idkzak', 'idtowr', 'empty'))
        indexes = [
            models.Index(fields=['wstrz', ]),
            models.Index(fields=['wskus', ]),
            models.Index(fields=['datzk', ]),
            models.Index(fields=['datos', ]),
            models.Index(fields=['kodkr', ]),
            models.Index(fields=['wertb', ]),
        ]
