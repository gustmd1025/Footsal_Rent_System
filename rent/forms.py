from django import forms

from rent.models import Place, RentInfo


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['pcode', 'pname', 'location', 'price', 'side', 'ball', 'vest', 'imgfile']
        labels = {
            'pcode': '풋살장 코드',
            'pname': '풋살장 이름',
            'location': '지역',
            'price': '가격',
            'side': '실내/실외',
            'ball': '공대여',
            'vest': '조끼대여',
            'imgfile': '이미지',
        }

class RentInfoForm(forms.ModelForm):
    class Meta:
        model = RentInfo
        fields = ['pcode', 'pname', 'price', 'r_date']
        labels = {
            'pcode': '풋살장 코드',
            'pname': '풋살장 이름',
            'price': '대여가격',
            'r_date': '대여날짜'
        }