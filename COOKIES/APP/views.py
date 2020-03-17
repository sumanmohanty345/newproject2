# from django.shortcuts import render,redirect
#
# def showmain(request):
#     total=len(request.COOKIES)
#     return render(request,"index.html",{"data":total})
#
# def addtocart(request):
#     p_no=request.GET.get('no')
#     p_name=request.GET.get('name')
#     response=redirect('main')
#     response.set_cookie(p_no,p_name)
#     return response
#
# def cartitems(request):
#     return render(request,"view.html")
#
# def delete(request):
#     pno=request.GET.get("no")
#     response=redirect('main')
#     response.delete_cookie(pno)
#     return response

from django.shortcuts import render,redirect

def showmain(request):
    total=len(request.COOKIES)
    return render(request,"index.html",{'data':total})


def addtocart(request):
    p_no=request.GET.get('no')
    p_name=request.GET.get('name')
    response=redirect('main')
    response.set_cookie(p_no,p_name)
    return response


def cartitems(request):
    return render(request,"view.html")


def delete(request):
    pno=request.GET.get('no')
    response=redirect('main')
    response.delete_cookie(pno)
    return response