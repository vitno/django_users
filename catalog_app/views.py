from django.shortcuts import render
from catalog_app.models import User



def index(request):

    users = User.objects.all()

    context = {
        'users': users
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):

    if request.method == 'POST':

        user = User(
            name=request.POST["name"],
            email=request.POST["email"],
        )
        user.save()

        context = {
            'name': user.name,
            'email': user.email,
        }

        return render(
            template_name='add_user_post.html',
            request=request,
            context=context,
        )

    latest = User.objects.latest('id').id
    last_visit = User.objects.get(id=latest)

    context = {
        'name': last_visit.name,
        'email': last_visit.email,
    }

    return render(
        template_name='add_user_get.html',
        request=request,
        context=context
    )

def get_user(request, user_id):
    users = User.objects.filter(id=user_id)

    context = {
        'users': users,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def edit_user(request, user_id):

    if request.method == 'POST':
        name = request.POST["name"],
        email = request.POST["email"]

        user = User.objects.get(id=user_id)

        user.name = name
        user.email = email
        user.save()

        context = {
            'name': name,
            'email': email,
        }

        return render(
            template_name='index.html',
            request=request,
            context=context
        )

    user = User.objects.get(id=user_id)

    context = {
        'name': user.name,
        'email': user.email,
    }

    return render(
        template_name='edit_user.html',
        request=request,
        context=context
    )
