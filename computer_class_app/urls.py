from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='index'),
    path('Participants.html', views.participants, name='Participants'),
    path('Teachers.html', views.teachers, name='Teachers'),
    path('Subjects.html', views.subjects, name='Subjects'),
    path('ProgressRecordBook.html', views.progressRecordBook, name='ProgressRecordBook'),
    path('Participants_Inputs.html', views.participantsInputs, name='Participants_Inputs'),
    path('Participants_Outputs.html', views.participantsOutputs, name='Participants_Outputs'),
    path('Participants_Updates.html', views.participantsUpdates, name='Participants_Updates'),
    path('Participants_Delete.html', views.participantsDelete, name='Participants_Delete'),
    path('Participants_InputsPy', views.participantsInputsPy, name='Participants_InputsPy'),
    path('Participants_OutputsPy', views.participantsOutputsPy, name='Participants_OutputsPy'),
    path('Participants_UpdatesPy', views.participantsUpdatesPy, name='Participants_UpdatesPy'),
    path('Participants_DeletePy', views.participantsDeletePy, name='Participants_DeletePy'),
    path('Teachers_Inputs.html', views.teachersInputs, name='Teachers_Inputs'),
    path('Teachers_Outputs.html', views.teachersOutputs, name='Teachers_Outputs'),
    path('Teachers_Updates.html', views.teachersUpdates, name='Teachers_Updates'),
    path('Teachers_Delete.html', views.teachersDelete, name='Teachers_Delete'),
    path('Teachers_InputsPy', views.teachersInputsPy, name='Teachers_InputsPy'),
    path('Teachers_OutputsPy', views.teachersOutputsPy, name='Teachers_OutputsPy'),
    path('Teachers_UpdatesPy', views.teachersUpdatesPy, name='Teachers_UpdatesPy'),
    path('Teachers_DeletePy', views.teachersDeletePy, name='Teachers_DeletePy'),
    path('Subjects_Inputs.html', views.subjectsInputs, name='Subjects_Inputs'),
    path('Subjects_Outputs.html', views.subjectsOutputs, name='Subjects_Outputs'),
    path('Subjects_Updates.html', views.subjectsUpdates, name='Subjects_Updates'),
    path('Subjects_Delete.html', views.subjectsDelete, name='Subjects_Delete'),
    path('Subjects_InputsPy', views.subjectsInputsPy, name='Subjects_InputsPy'),
    path('Subjects_OutputsPy', views.subjectsOutputsPy, name='Subjects_OutputsPy'),
    path('Subjects_UpdatesPy', views.subjectsUpdatesPy, name='Subjects_UpdatesPy'),
    path('Subjects_DeletePy', views.subjectsDeletePy, name='Subjects_DeletePy'),
    path('ProgressRecordBook_Inputs.html', views.progressRecordBookInputs, name='ProgressRecordBook_Inputs'),
    path('ProgressRecordBook_Outputs.html', views.progressRecordBookOutputs, name='ProgressRecordBook_Outputs'),
    path('ProgressRecordBook_Updates.html', views.progressRecordBookUpdates, name='ProgressRecordBook_Updates'),
    path('ProgressRecordBook_Delete.html', views.progressRecordBookDelete, name='ProgressRecordBook_Delete'),
    path('ProgressRecordBook_InputsPy', views.progressRecordBookInputsPy, name='ProgressRecordBook_InputsPy'),
    path('ProgressRecordBook_OutputsPy', views.progressRecordBookOutputsPy, name='ProgressRecordBook_OutputsPy'),
    path('ProgressRecordBook_UpdatesPy', views.progressRecordBookUpdatesPy, name='ProgressRecordBook_UpdatesPy'),
    path('ProgressRecordBook_DeletePy', views.progressRecordBookDeletePy, name='ProgressRecordBook_DeletePy'),
]