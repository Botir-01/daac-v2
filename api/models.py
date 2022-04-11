from django.db import models
from daac import settings


class Menu(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(null=True)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child')
    is_footer = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'menu'
        ordering = ['order']

    def __str__(self):
        path = [self.title]
        k = self.parent
        while k is not None:
            path.append(k.title)
            k = k.parent
        return ' -> '.join(path[::-1])


class MainPageSettings(models.Model):
    logo_title = models.CharField(max_length=200)
    logo = models.FileField(upload_to='uploads/settings')
    poster_title = models.CharField(max_length=200)
    poster_description = models.CharField(max_length=500)
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    telegram_link = models.URLField()
    icon = models.ImageField(upload_to='uploads/settings')
    rocket_icon = models.ImageField(upload_to='uploads/settings')
    poster_image_web = models.ImageField(upload_to='uploads/settings')
    poster_image_mobile = models.ImageField(upload_to='uploads/settings')
    poster_image_planshet = models.ImageField(upload_to='uploads/settings')
    second_poster_image = models.ImageField(upload_to='uploads/settings')
    second_poster_description = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Settings"

    def __str__(self):
        return "settings"

    @property
    def logo_url(self):
        if self.logo:
            return "%s%s" % (settings.HOST, self.logo.url)

    @property
    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)

    @property
    def rocket_icon_url(self):
        if self.rocket_icon:
            return "%s%s" % (settings.HOST, self.rocket_icon.url)

    @property
    def poster_image_web_url(self):
        if self.poster_image_web:
            return "%s%s" % (settings.HOST, self.poster_image_web.url)

    @property
    def poster_image_mobile_url(self):
        if self.poster_image_mobile:
            return "%s%s" % (settings.HOST, self.poster_image_mobile.url)

    @property
    def poster_image_planshet_url(self):
        if self.poster_image_planshet:
            return "%s%s" % (settings.HOST, self.poster_image_planshet.url)

    @property
    def second_poster_image_url(self):
        if self.second_poster_image:
            return "%s%s" % (settings.HOST, self.second_poster_image.url)


class Partner(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'partner'


class ServiceCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/service')
    icon = models.ImageField(upload_to='uploads/service')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    @property
    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service_category'


class Service(models.Model):
    title = models.CharField(max_length=255)
    service_category_id = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service'


class Stage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='uploads/stage')
    service_category_id = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='stages')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'stage'


class ProjectCategory(models.Model):
    title = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "project_category"


class Project(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/project')
    project_category_id = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'


class DirectionCategory(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/direction')
    background_image = models.ImageField(upload_to='uploads/direction')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    @property
    def background_image_url(self):
        if self.background_image:
            return "%s%s" % (settings.HOST, self.background_image.url)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'direction_category'
        ordering = ['order']


class Task(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    icon = models.ImageField(upload_to='uploads/direction')
    direction_category_id = models.ForeignKey(DirectionCategory, on_delete=models.CASCADE, related_name='tasks')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)

    class Meta:
        db_table = 'task'


class Application(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    file = models.FileField(upload_to='uploads/application')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def file_url(self):
        if self.file:
            return "%s%s" % (settings.HOST, self.file.url)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'application'


class Feedback(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'feedback'


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/employee')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image:
            return "%s%s" % (settings.HOST, self.image.url)

    @property
    def full_name(self):
        if self.first_name and self.second_name:
            return '%s %s' % (self.first_name, self.second_name)

    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.first_name

    class Meta:
        db_table = 'employee'


class Contact(models.Model):
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=400)
    foundation_date = models.DateTimeField()
    clients_number = models.IntegerField()
    employee_number = models.IntegerField()
    projects_number = models.IntegerField()
    technical_support = models.IntegerField()
    icon = models.ImageField(upload_to='uploads/contact')
    short_video = models.FileField(upload_to='uploads/contact')
    file = models.FileField(upload_to='uploads/contact')
    file_name = models.CharField(max_length=300)

    def file_url(self):
        if self.file:
            return "%s%s" % (settings.HOST, self.file.url)

    def icon_url(self):
        if self.icon:
            return "%s%s" % (settings.HOST, self.icon.url)

    def short_video_url(self):
        if self.short_video:
            return "%s%s" % (settings.HOST, self.short_video.url)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'contact'

