from django.db import models


class Experiment(models.Model):

    subject_list = [('Physics', 'Physics'), ('Chemistry', 'Chemistry'),
                    ('Biology', 'Biology'), ('Gneral Science', 'Gneral Science'), ]

    title = models.CharField(max_length=1000)
    one_liner = models.CharField(max_length=10000)
    dificulty = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    subject = models.CharField(
        choices=subject_list, max_length=100, null=True)
    main_image = models.ImageField(null=True, blank=True, upload_to="static/")
    precautions = models.TextField(default='follow general safety precautions')

    def __str__(self) -> str:
        return self.title


class MaterialsList(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return str(self.name)+' ('+str(self.experiment)+')'


class Procedure(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    step_number = models.IntegerField()
    step_image = models.ImageField(null=True, blank=True, upload_to="static/")
    description = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return str(self.experiment)+' '+str(self.step_number)
