import os
from django.http import JsonResponse
from django.views import View


class MemView(View):
    def get(self, request):
        os.system(f"{os.getcwd()}/apps/meninfo/mem_bash.sh")
        with open(f'{os.getcwd()}/apps/meninfo/mem_bash.html', 'r', encoding='utf-8') as f:
            data = f.readlines()
            mem_list = []
            for i in data:
                l1 = i.split("&")
                l2 = []
                for j in l1:
                    l2.append(j.split("!")[1])
                d = {"mem_used": l2[0], "mem_cache": l2[1], "mem_buffer": l2[2], "Time": l2[3]}
                mem_list.append(d)

        return JsonResponse(mem_list, safe=False)
