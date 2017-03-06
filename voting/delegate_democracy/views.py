from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Body, Voter


def hello_world(request):
    return HttpResponse("Hello, world. You're at the delegate democracy test page.")

@login_required
def voting_body(request):
    if request.method == 'POST':
        voting_body = Body()
        voting_body.name = request.POST['voting_body_name']
        voting_body.save()
        voter = Voter()
        voter.user = request.user
        voter.body = voting_body
        voter.body_admin = True
        voter.save()
    voting_body_list = Body.objects.filter(voter__user=request.user).all()
    context = {'voting_body_list': voting_body_list,
               'user': request.user}
    return render(request, 'delegate_democracy/voting_body.html', context)

def voting_body_detail(request):
    pass