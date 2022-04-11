from rest_framework import serializers
from .models import Menu, MainPageSettings, Partner, ServiceCategory, Service, Stage, ProjectCategory, Project, \
                    DirectionCategory, Task, Application, Feedback, Employee, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['description', 'email', 'address', 'phone_number']


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'url']


class MenuSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'url', 'child'],

    def get_child(self, obj):
        sub_menu = Menu.objects.filter(parent=obj)
        if sub_menu.exists():
            return SubMenuSerializer(sub_menu, many=True).data
        return []


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageSettings
        fields = ['logo_title', 'logo_url', 'poster_title', 'poster_description', 'instagram_link', 'facebook_link',
                  'telegram_link', 'icon_url', 'rocket_icon_url', 'poster_image_web_url', 'poster_image_mobile_url',
                  'poster_image_planshet_url', 'second_poster_image_url', 'second_poster_description']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title', 'link']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title']


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ['title', 'description', 'image_url', 'icon_url', 'services']


class ServiceCategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['title', 'image_url']


class DirectionCategoryMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionCategory
        fields = ['title', 'order', 'background_image_url', 'image_url']


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['description', 'email', 'address', 'phone_number', 'file_name', 'file_url']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'link', 'image_url', 'project_category_id']


class ProjectCategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectCategory
        fields = ['id', 'title', 'projects']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['full_name', 'title', 'image_url']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['description', 'phone_number', 'foundation_date', 'clients_number', 'employee_number',
                  'projects_number', 'technical_support', 'short_video'
                  ]


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['icon', 'phone_number', 'email', 'address', 'longitude', 'latitude']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['title', 'description']


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['title', 'description', 'icon_url']


class ServicePageSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    stages = StageSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ['title', 'description', 'image_url', 'icon_url', 'services', 'stages']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'icon']


class DirectionSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = DirectionCategory
        fields = ['title', 'description', 'image_url', 'background_image_url', 'tasks']


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['name', 'phone_number', 'email', 'message', 'file']
