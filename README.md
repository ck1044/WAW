2-01 URL과 뷰
    -django-admin startapp pybo
    -config/urls.py 파일에 URL매핑정보를 추가하는 것이다.
        -페이지 요청 발생 → URL과 뷰 함수간의 매핑을 정의!(뷰=views.py)
        -urlpatterns에 path()경로 추가
        -뷰 함수 호출! ( views.py를 디렉토리로 바꾼 후 세부화 하기)
    -django-admin startproject config .
    -python manage.py runserver
    -python manage.py migrate

2-02 모델
    -제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용해야 한다. 내용(content)처럼 글자수를 제한할 수 없는 텍스트는 위처럼 TextField를 사용해야 한다.
        -해시태그 → CharField
        -내용 → TextField 

2-03 장고 관리자
    -python manage.py createsuperuser
    -waw 모델 → admin 등록하기
    -모델 검색!
        -search_fields = [‘검색하려는변수’]
    -admin.site.register(해당Admin class추가!)

2-04 목록 조회
    -render 함수는 조회된 질문목록 데이터를 waw/post_list.html 파일에 적용하여 HTML로 변환해 주는 함수이다. 
    -템플릿 디렉토리
        -여기서 사용된 waw/post_list.html 파일을 템플릿이라고 부른다.
        -템플릿 파일은 HTML파일과 비슷하지만 장고에서 사용하는 태그들을 사용할수 있는 HTML파일이다.
        -템플릿을 저장할 디렉토리는 config/settings.py 파일의 TEMPLATES 항목에 추가해 주어야 한다.
        -'DIRS': [BASE_DIR / 'templates'],
        -BASE_DIR : c :/projects/waw
        -공통 템플릿 디렉토리 - C:\projects\waw\templates
        -waw 앱 템플릿 디렉토리 - C:\projects\waw\templates\waw
    -템플릿 태그
        -{% if %}, {% endif %}
        -{% for %}, {% endfor %}
        -{{객체}}, {{객체.속성}}
    -상세조회
        -urls.py → path(int:post_id에 저장, views.detail 함수 실행)
 
 
