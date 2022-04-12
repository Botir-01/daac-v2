from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from .models import Menu, MainPageSettings, Partner, ServiceCategory, ProjectCategory, DirectionCategory, Application,\
                    Feedback, Employee, Contact
from .serializers import MenuSerializer, MainPageSerializer, PartnerSerializer, ServiceCategorySerializer, \
                    ServiceCategoryMainSerializer, DirectionCategoryMainSerializer, FooterSerializer, \
                    ProjectCategorySerializer, AboutSerializer, EmployeeSerializer, ContactsSerializer, \
                    FeedbackSerializer, ServicePageSerializer, DirectionSerializer, ApplicationSerializer, \
                    AboutMainSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset

        return queryset


class MainPageView(CustomModalViewSet):
    queryset = MainPageSettings.objects.all()
    serializer_class = MainPageSerializer
    pagination_class = None
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        obj = Menu.objects.filter(parent__isnull=True)
        serializer = self.serializer_class
        object_serializer = MenuSerializer
        service_categories = ServiceCategory.objects.all()
        direction_categories = DirectionCategory.objects.all()
        about = Contact.objects.all()
        payload = {
            'site': serializer(instance).data,
            'service_categories': ServiceCategoryMainSerializer(service_categories, many=True).data,
            'menu': object_serializer(obj, many=True).data,
            'directions': DirectionCategoryMainSerializer(direction_categories, many=True).data,
            'about': AboutMainSerializer(about, many=True).data
        }
        return Response(payload)


class PartnerView(CustomModalViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    pagination_class = None
    http_method_names = ['get']


class ServiceCategoryView(CustomModalViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    pagination_class = None
    http_method_names = ['get']


class FooterView(CustomModalViewSet):
    queryset = Contact.objects.all()
    serializer_class = FooterSerializer
    pagination_class = None
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        obj = Menu.objects.filter(parent__isnull=True, is_footer=True)
        serializer = self.get_serializer_class()
        object_serializer = MenuSerializer
        payload = {
            'footer': serializer(instance).data,
            'menu': object_serializer(obj, many=True).data,
        }
        return Response(payload)


class ProjectCategoryView(CustomModalViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    pagination_class = None
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['id']


class AboutView(CustomModalViewSet):
    queryset = Contact.objects.all()
    serializer_class = AboutSerializer
    pagination_class = None
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        obj = Employee.objects.all()
        serializer = self.get_serializer_class()
        object_serializer = EmployeeSerializer
        payload = {
            'about': serializer(instance).data,
            'employees': object_serializer(obj, many=True).data,
        }
        return Response(payload)


class ContactsView(CustomModalViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = None
    http_method_names = ['get']


class FeedbackView(CustomModalViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = None
    http_method_names = ['get']


class ServicePageView(CustomModalViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServicePageSerializer
    pagination_class = None
    http_method_names = ['get']


class DirectionView(CustomModalViewSet):
    queryset = DirectionCategory.objects.all()
    serializer_class = DirectionSerializer
    pagination_class = None
    http_method_names = ['get']


class ApplicationViewset(viewsets.ViewSet, CustomModalViewSet, generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        instance = Application.objects.all()
        return Response(ApplicationSerializer(instance, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = Application.objects.create(**serializer.validated_data)
            payload = {
                'success': 'Application is send successfully'
            }
            return  Response(payload, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)