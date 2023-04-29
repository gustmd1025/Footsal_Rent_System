from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Place,RentInfo
from .forms import PlaceForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count

def index(request):

    """
    rent 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')     # 페이지
    kw = request.GET.get('kw', '')      # 검색어
    so = request.GET.get('so', 'recent')    # 정렬 기준

    if so == 'recommend':
        place_list = Place.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', 'pcode')
    elif so == 'popular':
        place_list = Place.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', 'pcode')
    else:  # recent
        place_list = Place.objects.order_by('pcode')

    # 조회
    if kw:
        place_list = place_list.filter(
            Q(location__icontains=kw) |                      # 제목 검색
            Q(pname__icontains=kw)                       # 내용 검색
        ).distinct()

    paginator = Paginator(place_list, 10)
    page_obj = paginator.get_page(page)
    context = {'place_list' : page_obj}
    return render(request, 'rent/place_list.html', context)

def detail(request,place_id):
    """
    rent 내용 출력
    """
    place = get_object_or_404(Place, pk=place_id)
    context = {'place': place}
    return render(request, 'rent/place_detail.html', context)

@login_required(login_url='common:login')
def place_create(request):
    """
    place 제품 등록
    """
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user # 추가한 속성 author 적용
            place.save()
            return redirect('rent:index')
    else:
        form = PlaceForm()
    context = {'form': form}
    return render(request, 'rent/place_form.html', context)

@login_required(login_url='common:login')
def place_modify(request, place_id):
    """
    place 제품 수정
    """
    place = get_object_or_404(Place, pk=place_id)
    if request.user != place.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('rent:detail', place_id=place.id)

    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.modify_date = timezone.now()  # 수정일시 저장
            place.save()
            return redirect('rent:detail', place_id=place.id)
    else:
        form = PlaceForm(instance=place)
    context = {'form': form}
    return render(request, 'rent/place_form.html', context)


@login_required(login_url='common:login')
def place_delete(request, place_id):
    """
    place 제품 삭제
    """
    place = get_object_or_404(Place, pk=place_id)
    if request.user != place.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('rent:detail', place_id=place.id)
    place.delete()
    return redirect('rent:index')


def info_index(request):

    """
    rent 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')     # 페이지
    kw = request.GET.get('kw', '')      # 검색어
    so = request.GET.get('so', 'recent')    # 정렬 기준

    if so == 'recommend':
        rentinfo_list = RentInfo.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', 'r_date')
    elif so == 'popular':
        rentinfo_list = RentInfo.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', 'r_date')
    else:  # recent
        rentinfo_list = RentInfo.objects.order_by('-r_date')

    # 조회
    if kw:
        rentinfo_list = rentinfo_list.filter(
            Q(pcode__icontains=kw) |                      # 제목 검색
            Q(pname__icontains=kw)                       # 내용 검색
        ).distinct()

    paginator = Paginator(rentinfo_list, 10)
    page_obj = paginator.get_page(page)
    context = {'rentinfo_list' : page_obj}
    return render(request, 'rent/rentinfo_list.html', context)