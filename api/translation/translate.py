from modeltranslation.translator import TranslationOptions, register
from api.models import Menu, MainPageSettings, Partner, ServiceCategory, Service, Stage, ProjectCategory, Project, \
                        DirectionCategory, Task, Feedback, Employee, Contact


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(MainPageSettings)
class MainPageSettingsTranslationOptions(TranslationOptions):
    fields = ('logo_title', 'poster_title', 'poster_description', 'second_poster_description', )


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Stage)
class StageTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(DirectionCategory)
class DirectionCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Task)
class TaskTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('first_name', 'second_name', 'title', )


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('description', 'address', 'file_name', )
