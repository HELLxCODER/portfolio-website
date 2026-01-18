from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated (e.g., Python, NumPy, Pandas)")
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, help_text="Coursera, Udemy, etc.")
    description = models.TextField()
    date_obtained = models.DateField()
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True, help_text="Link to the online cerificate")


    class Meta:
        ordering = ['-date_obtained']

    def __str__(self):
        return f"{self.title} - {self.issuer}"