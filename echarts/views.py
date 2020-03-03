from collections import Counter
import random

from django.shortcuts import render
from .models import Newzhaopin


def index(request):
    # 累计爬取的条数,返回all_job_counts
    all_job_counts = Newzhaopin.objects.all().count()

    # 统计每种工作的数量,返回job_name和jobs_counts
    job_name = ['python', 'java', 'php', 'web', 'sql', 'swift']
    jobs_counts = []
    for i in job_name:
        jobs_counts.append(Newzhaopin.objects.filter(position__icontains=i).count())
    # print(jobs_counts)
    jobs_class = list(zip(job_name, jobs_counts))

    # 统计城市出现的次数,返回city_count,city
    all_cities = []
    city = []
    all_info = Newzhaopin.objects.all()
    for i in all_info:
        all_cities.append(i.workspace)
        if i.workspace not in city:
            city.append(i.workspace)
    # print(city)
    city_count = Counter(all_cities)

    list1 = city_count.keys()
    list2 = city_count.values()
    city_class = list(zip(list1, list2))
    # print(list1)
    # print(list2)
    # print(city_class)

    # 随机一条数据
    sj = random.randint(0, all_job_counts)
    # print(sj)
    suiji = Newzhaopin.objects.all()[sj]
    # print(suiji.comname, suiji.workspace, suiji.position, suiji.maxsalary,
    #       suiji.publish, suiji.link)
    workspace = suiji.workspace
    comname = suiji.comname
    publish = suiji.publish
    maxsalary = suiji.maxsalary
    position = suiji.position
    link = suiji.link

    return render(request, 'echarts/index.html',
                  {"job_counts": all_job_counts,
                   'job_name': job_name,
                   "jobs_class": jobs_class,
                   "city_class": city_class,
                   'workspace': workspace,
                   'comname': comname,
                   'publish': publish,
                   'maxsalary': maxsalary,
                   'position': position,
                   'link': link,
                   })
