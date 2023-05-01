from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path("allSkills/", views.get_skill_set),
               path("newmeeting/", views.get_schedule_meeting_page,
                    name='new-meeting'),
               path('fetch-occupancies/', views.get_occupancies, name='fetch-occ'),
               path("my-calendar/", views.get_calendar, name='calendar'),
               path('fetch-data/', views.get_events, name='fetch_data'),
               path("editCourses/", views.submit_courses, name='edit-courses'),
               path("proj-desc/", views.get_project, name='project-page'),
               path("search/", views.get_search, name='search-page'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
