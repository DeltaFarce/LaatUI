import os

from django.http import JsonResponse
from django.views import View


class TopView(View):
    def get(self, request):
        os.system(f"{os.getcwd()}/apps/tops/top_bash.sh")
        with open(f'{os.getcwd()}/apps/tops/top_bash.html', 'r', encoding='utf-8') as f:
            data = f.readlines()
            mem_list = []
            for i in data:
                l1 = i.split("&")
                l2 = []
                for j in l1:
                    l2.append(j.split("!")[1])
                d = {"PID": l2[0], "USER": l2[1], "%CPU": l2[2], "%MEM": l2[3], "COMMAND": l2[4], "Time": l2[5]}
                mem_list.append(d)

        return JsonResponse(mem_list, safe=False)