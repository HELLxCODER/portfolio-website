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


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    proficiency = models.IntegerField(help_text="Skill level from 0 to 100")
    icon_class = models.CharField(max_length=100, help_text="Bootstrap icon class (e.g., bi-code-slash)")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.proficiency}%"
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, help_text="Leave blank if ongoing")
    description = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True, help_text="GPA or Percentage")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")

    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} at {self.institution}"
    
    @property
    def is_ongoing(self):
        return self.end_date is None