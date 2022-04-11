from django.urls import path, include
from rest_framework import routers
from .views import MainPageView, PartnerView, FooterView, ServiceCategoryView, ProjectCategoryView, AboutView, \
                    ContactsView, FeedbackView, ServicePageView, DirectionView, ApplicationViewset

router = routers.DefaultRouter()
router.register(r'main-page', MainPageView)
router.register(r'partners', PartnerView)
router.register(r'footer', FooterView)
router.register(r'services', ServiceCategoryView)
router.register(r'projects', ProjectCategoryView)
router.register(r'about', AboutView)
router.register(r'contacts', ContactsView)
router.register(r'feedback', FeedbackView)
router.register(r'service-page', ServicePageView)
router.register(r'directions', DirectionView)
router.register(r'application', ApplicationViewset)

urlpatterns = [
    path('', include(router.urls)),
]