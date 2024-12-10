from django.urls import path,include
from .views import *
from rest_framework import routers
router=routers.SimpleRouter()


router.register(r'online',Online_Examination_SystemViewSet,basename='online_list')

router.register(r'user',UserProfileViewSet,basename='user_list')

router.register(r'student',StudentViewSet,basename='student_list')

router.register(r'questions',QuestionsViewSet,basename='questions_list')

router.register(r'courses',CoursesViewSet,basename='courses_list')

router.register(r'course',CourseViewSet,basename='course_list')

router.register(r'lesson',LessonViewSet,basename='lesson_list')

router.register(r'course_video',CourseVideoViewSet,basename='course_video_list')

router.register(r'lesson_video',LessonVideoViewSet,basename='lesson_video_list')

router.register(r'exam',ExamViewSet,basename='exam_list')

router.register(r'certificate',CertificateViewSet,basename='certificate_list')

router.register(r'favorite',FavoriteViewSet,basename='favorite_list')

router.register(r'cart',CartViewSet,basename='cart_list')

router.register(r'carcourse',CarCourseViewSet,basename='carcourse_list')

router.register(r'teacher',TeachersViewSet,basename='teacher_list')

router.register(r'teacher_schedule',Teachers_ScheduleViewSet,basename='teacher_schedule_list')

router.register(r'subscription',SubscriptionViewSet,basename='subscription_list')

router.register(r'course_pricing',CoursePricingViewSet,basename='course_pricing_list')

router.register(r'exam_result',ExamResultViewSet,basename='exam_result_list')

router.register(r'study_group',StudyGroupViewSet,basename='study_group_list')

router.register(r'attendance',AttendanceViewSet,basename='attendance_list')

router.register(r'homework',HomeworkViewSet,basename='homework_list')


urlpatterns=[
    path('',include(router.urls)),
]