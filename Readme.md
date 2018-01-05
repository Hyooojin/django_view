# Django

## View

view를 추가 작성하는데서 계속해서 error가 나서 해보는 **django tutorial**

주된 참고 페이지: [첫 번째 장고 앱 작성하기, part3](https://docs.djangoproject.com/ko/2.0/intro/tutorial03/)

### View Page 추가하기 

* polls/views.py

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

* polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

<br>

<details>

<summary> view 추가 작성 차근차근 따라하기</summary>

index외에 다른 Page들을 추가 작성하고 싶을 때는 다른 view를 정의하고, 그에 맞는 url pattern을 지정해 주면 된다. 

지금부터 index를 빼고, detail, results, vote 페이지를 추가 작성 해 보겠다. 
모든 페이지: index, detail, results, vote
추가할 페이지: detail, results, vote

#### 1. 페이지를 추가하기 전 polls/views.py와 urls.py

* polls/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! ")
```

* polls/urls.py

```python
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
]
```

http://localhost:8000/polls 를 돌리면 index page가 뜬다. 

```
Hello, world! 
```

#### 2. page를 추가한 후 views.py와 urls.py

* views.py

```python
from django.http import HttpResponse

# Create your views here
def index(request):
    return HttpResponse("Hello, world! ")

def detail(request):
    return HttpResponse("detail page using HttpResponse")

def results(request):
    response = "response page using valiable and HttpResponse."
    return HttpResponse(response)

def vote(request):
    return HttpResponse("vote page using HttpResponse")
```

* urls.py

```python
from django.urls import path
from . import views

urlpattenrs=[
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]
```

* 화면
* `http://localhost:8000/polls`

```
Hello, world!
```

* `http://localhost:8000/polls/detail`

```
detail page using HttpResponse
```

* `http://localhost:8000/polls/results/`

```
response page using valiable and HttpResponse.
```

* `http://localhost:8000/polls/vote/`

```
vote page using HttpResponse
```

#### 3. request외 파라미터 추가 

* polls/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! ")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "Yor're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

* urls.py

```python
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]    
```

* 화면
* `http://localhost:8000/polls/1/`

```
You're looking at question 1.

# 만약 http://localhost:8000/polls/2/
# You're looking at question 2.
```

* `http://localhost:8000/polls/2/results/`

```
Yor're looking at the results of question 2.
```

* `http://localhost:8000/polls/3/vote/`

```
You're voting on question 3.
```

> \<int:question_id\> 부분에는 입력하는 값 그대로가 출력된다. 
>
> ```
> 문자열의 :question_id> 부분은 일치되는 패턴을 구별하기 위해 정의한 이름이며, <int: 부분은 어느 패턴이 해당 URL 경로에 일치되어야 하는 지를 결정하는 컨버터입니다.
> ```
>
> %s 는 문자열 포매팅이다.
> 예시
>
> ```python
> >>> "I eat %s apples." % "five"
> 'I eat five apples.'
> ```



</details>

### View가 할 수 있는 것들

* 각 view는 요청된 페이지의 내용이 담긴 HttpResponse객체를 반환하거나,  Http404 같은 예외를 발생하게 한다.
* <span style="color:tomato">자유롭게</span> view가 어떤 행동을 하도록 할 수 있다. 
* 데이터베이스의 레코드를 읽을 수도 있다.
* Django나 python에서 서드파티로 제공되는 태플릿 시스템을 사용할 수 있다. 
* PDF를 생성하거나, XML 출력을 하거나, 실시간으로 ZIP 파일을 만들 수 있다. 
* view는 원하는 무엇이든, Python의 어떤 라이브러리던 사용할 수 있다. 
* .....

<p style="color:tomato">모든 Django는 <u>HttpResponse</u>객체나, 혹은 <u>예외(execption)</u>을 원한다.</p>



### 코드와 디자인을 분리
view에서 <u>페이지의 디자인이 하드코딩</u> 되어있다면 문제가 생긴다.  만약 페이지가 보여지는 방식을 바꾸고 싶다면, python코드를 편집해야하는데.. 

이때, <span style="color:tomato">view가 사용할 수 있는 탬플릿을 작성</span>하여, <span style="color:tomato">Python 코드로부터 디자인을 분리</span>하도록 Django의 탬플릿 시스템을 사용해 볼 것이다. 

>1. view가 사용할 수 있는 탬플릿 작성
>2. python 코드로 부터 디자인을 분리

* polls/views.py 에 추가 
  <p style="color:grey">polls/views.py페이지에 하드코드 되어 있는 상태</p>

```python
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

화면 

```
b_question, a_question
```



* polls/templates/polls/index.html
  <p style="color:grey">탬플릿에 코드 입력</p>

```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

* polls/views.py
  <p style="color:grey">template을 이용하여 polls/views.py에 index view를 업데이트</p>

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

화면

```python
* b_question
* a_question
```

<p style="color:grey"> [question] Django 탬플릿을 사용할 때는 무조건 HttpResponse(template.render(context, request))가 되어야 하는 걸까? </p>

<details>

<summary>하드코딩에서 Django 탬플릿 시스템 사용을 사용하기 위한 <strong>코드 편집</strong></summary>

주 참고 페이지: [첫 번째 장고 앱 작성하기, part3 - view가 실제로 뭔가 하도록 만들기](https://docs.djangoproject.com/ko/2.0/intro/tutorial03/)

### 1. `polls` 디렉토리에 `templates`  디렉토리 만들기.. 그 안에 `polls`디렉토리 만들기

Django는 여기서 템플릿을 찾게 될 것이다. 
<p style="color:grey">만약 Django가 어떻게 template를 불러오고 랜더링 할 것인지 알고 싶다면 project의 TEMPLATES를 참고</p>

1. `polls`디렉토리에 `templates`디렉토리를 만든다. 
2. `templates`디렉토리에 `polls`디렉토리를 만든다.
3. `polls`/`templates`/`polls` 에 index.html을 만든다. 
4. template은 `polls/templates/polls/index.html`과 같은 형태가 된다.

### 2. 탬플릿에 코드 입력

* polls/templates/polls/index.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
Hello world!
</body>
</html>
```

### 3. `views.py`에서 index view를 업데이트

* polls/views.py

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(request))
```



</details>