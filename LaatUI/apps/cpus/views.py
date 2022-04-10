import os
from django.http import JsonResponse
from django.views import View


class CpuView(View):
    def get(self, request):
        os.system(f"{os.getcwd()}/apps/cpus/cpu_bash.sh")
        with open(f'{os.getcwd()}/apps/cpus/cpu_bash.html', 'r', encoding='utf-8') as f:
            data = f.readlines()
            mem_list = []
            for i in data:
                l1 = i.split("&")
                l2 = []
                for j in l1:
                    l2.append(j.split("!")[1])
                d = {"US": l2[0], "SY": l2[1], "Free": l2[2], "Time": l2[3]}
                mem_list.append(d)

        return JsonResponse(mem_list, safe=False)