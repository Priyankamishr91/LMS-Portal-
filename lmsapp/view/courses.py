from django.shortcuts import render
from lmsapp.models import Course, Video, UserCourse
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class MyCoursesList(ListView):
    template_name= 'courses/my_courses.html'
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)

def coursepage(request, slug):
    course=Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos=course.video_set.all().order_by("serial_number")
    next_lecture = 2
    prev_lecture =None;
    if serial_number is None:
        serial_number=1
    else:
        next_lecture=int(serial_number)+1
        if len(videos)<next_lecture:
            next_lecture = None

        prev_lecture=int(serial_number)-1

    video= Video.objects.get(serial_number = serial_number, course = course)

    if (video.is_preview is False):
        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user, course = course)
            except:
                return redirect("checkout", slug=course.slug)

    context={
        "course" : course,
        "video" : video,
        "videos" : videos,
        "next_lecture": next_lecture,
        "prev_lecture": prev_lecture
    }
    return render(request, template_name="courses/coursePage.html", context=context)