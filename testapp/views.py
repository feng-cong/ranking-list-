from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp import models
# Create your views here.

class Test(APIView):
    """
    存储数据
    name 获取用户输入的名字
    score 获取用户输入的分数
    """
    def post(self,request):
        name =  request.POST.get('name')
        score =  request.POST.get('score')
        print(name)
        models.Test.objects.create(
            name = name,
            score = score
        )

        return Response({'ok':'ok'})

class Test_Order_By(APIView):
    """
    取出数据进行排序
    a2 返回给前端排序后的数据
    tst1 当前用户的数据
    tst3 得到所有数据的长度列表
    
    """
    def get(self,request):
        name = request.GET.get('name')
        tst1 = models.Test.objects.get(name=name)

        tst2 = models.Test.objects.order_by('-score')

        tst3 = [str(i) for i in range(1,len(tst2)+1)]

        a2=dict(zip(tst3,tst2)) 
     
        return render(request,'test_order_by.html',locals())