import os
from django.http import JsonResponse
from django.views import View


class LoadView(View):
    def get(self, request):
        os.system(f"{os.getcwd()}/apps/loads/load_bash.sh")
        with open(f'{os.getcwd()}/apps/loads/load_bash.html', 'r', encoding='utf-8') as f:
            data = f.readlines()
            print(data)
            mem_list = []
            for i in data:
                l1 = i.split(",")
                l2 = []
                for j in l1:
                    print(j)
                    l2.append(j.split("!")[1])
                d = {"load_5": l2[0], "load_10": l2[1], "load_15": l2[2], "Time": l2[3]}
                mem_list.append(d)

        return JsonResponse(mem_list, safe=False)