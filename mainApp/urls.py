from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('index', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search' ),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^wallet/$', views.wallet, name='wallet'),
    url(r'^book/(?P<pk>\d+)/$', views.book, name='book'),
    url(r'^book/confirmation/(?P<pk>\d+)/$', views.confirmation, name='confirmation'),
    url(r'^managewallet/$', views.manageWallet),
    url(r'^maketutor/$', views.makeTutor),
    url(r'^book/confirmbooking/$', views.confirmBooking),
    url(r'^profile/tutor/(?P<pk>\d+)/$', views.tutorProfile),
    url(r'^cancel/(?P<pk>\d+)/$', views.cancel, name='cancel'),
    url(r'^transactionhistory/$', views.transactionHistory),
    url(r'^managecourses/$', views.courses, name='courses'),
    url(r'^addcourse/$', views.addCourse),
    url(r'^removecourses/$', views.removeCourses),
    url(r'^getUniCourses/$', views.get_uni_courses),
    url(r'^activateTutor/', views.activate_deactivate_tutor),
    url(r'^manageschedule/$', views.manageSchedule),
    url(r'^addunavailable/$', views.addUnavailable),
    url(r'^removeunavailable/$', views.removeUnavailable),
    url(r'^resetpwdtoken/$', views.getResetPwdToken),
    url(r'^resetpwd/$', views.resetPwd),
    url(r'^setnewpwd/$', views.setNewPwd),
    url(r'^managetags/$', views.tags, name='tags'),
    url(r'^addtag/$', views.addTag),
    url(r'^removetags/$', views.removeTags),
    url(r'^review/(?P<pk>\d+)/$', views.review, name='review'),
    url(r'^addreview/(?P<pk>\d+)/$', views.addReview),
    url(r'^admin/$', views.admin),
    url(r'^admin/withdraw/$', views.adminWithdraw),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
