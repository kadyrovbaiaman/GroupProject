from django.contrib import admin
from .models import *

class QuestionsInline(admin.TabularInline):
    model=Questions
    extra=1

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]

admin.site.register(Exam,ExamAdmin)



admin.site.register(Online_Examination_System)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseVideo)
admin.site.register(LessonVideo)
admin.site.register(Homework)
admin.site.register(Certificate)
admin.site.register(Favorite)
admin.site.register(Cart)
admin.site.register(CarCourse)

admin.site.register(Teachers)
admin.site.register(Teachers_Schedule)
admin.site.register(Subscription)
admin.site.register(CoursePricing)
admin.site.register(StudyGroup)
admin.site.register(Attendance)
admin.site.register(ExamResult)
admin.site.register(CourseReview)

