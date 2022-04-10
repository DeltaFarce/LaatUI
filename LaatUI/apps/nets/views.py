import os
from django.http import JsonResponse
from django.views import View


class NetView(View):
    def get(self, request):
        os.system(f"{os.getcwd()}/apps/nets/net_bash.sh")
        with open(f'{os.getcwd()}/apps/nets/net_bash.html', 'r', encoding='utf-8') as f:
            data = f.readlines()
            mem_list = []
            for i in data:
                l1 = i.split("&")
                l2 = []
                for j in l1:
                    l2.append(j.split("!")[1])
                d = {"RX": l2[0], "TX": l2[1], "Time": l2[2]}
                mem_list.append(d)

        return JsonResponse(mem_list, safe=False)
