from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.Home, name='index'),
    path('', views.Dashboard, name='index'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('password', views.change_password, name='password'),
    path('profile', views.profile, name='profile'),
    path('settings', views.Settings, name='settings'),

    path('dashboard' , views.Dashboard, name='dashboard'),

    path('tasks', views.TaskList, name='task-list'),

    path('reporttemplate', views.ReportTemplateList.as_view(), name='report-template-list'),
    path('reporttemplate/add/', views.ReportTemplateCreate.as_view(), name='report-template-add'),
    path('reporttemplate/<int:pk>/', views.ReportTemplateUpdate.as_view(), name='report-template-update'),
    path('reporttemplate/<int:report_template_id>/delete', views.ReportTemplateDelete, name='report-template-delete'),
    
    path('projects', views.ProjectList.as_view(), name='project-list'),
    path('project/add/', views.ProjectCreate.as_view(), name='project-add'),
    path('project/<int:pk>/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:project_id>/delete', views.ProjectDelete, name='project-delete'),
    path('project/<int:project_id>/report', views.ProjectReport, name='project-report'),

    path('project/<int:project_id>/note/add', views.ProjectNoteCreate, name='project-note-add'),
    path('project/<int:project_id>/note/<int:note_id>/update', views.ProjectNoteUpdate, name='project-note-update'),
    path('project/<int:project_id>/note/<int:note_id>/delete', views.ProjectNoteDelete, name='project-note-delete'),
    path('project/<int:project_id>/note/upload', views.ProjectNoteUpload, name='project-note-upload'),

    path('project/<int:project_id>/tasks', views.ProjectTaskList, name='project-task-list'),
    path('project/<int:project_id>/task/add', views.ProjectTaskCreate, name='project-task-add'),
    path('project/<int:project_id>/task/<int:task_id>/update', views.ProjectTaskUpdate, name='project-task-update'),
    path('project/<int:project_id>/task/<int:task_id>/delete', views.ProjectTaskDelete, name='project-task-delete'),

    path('templates', views.TemplateList.as_view(), name='template-list'),
    path('template/add/', views.TemplateCreate.as_view(), name='template-add'),
    path('template/<int:pk>/', views.TemplateUpdate.as_view(), name='template-update'),
    path('template/<int:template_id>/delete', views.TemplateDelete, name='template-delete'),

    path('json/notes/<int:project_id>/', views.noteMenu, name='note-menu'),
    path('notes', views.NoteList.as_view(), name='note-list'),
    path('note/add/', views.NoteCreate.as_view(), name='note-add'),
    path('note/<int:pk>/', views.NoteUpdate.as_view(), name='note-update'),

]
