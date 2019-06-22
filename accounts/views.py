from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')
