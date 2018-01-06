# Django

## View

view를 추가 작성하는데서 계속해서 error가 나서 해보는 **django tutorial**

주된 참고 페이지: [첫 번째 장고 앱 작성하기, part3](https://docs.djangoproject.com/ko/2.0/intro/tutorial03/)

<br>

<br>

<br>

### View Page 추가하기 

<hr>

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
<br>
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

<summary> <strong>view 추가 작성 차근차근 따라하기</strong></summary>
<br>

index외에 다른 Page들을 추가 작성하고 싶을 때는 다른 view를 정의하고, 그에 맞는 url pattern을 지정해 주면 된다. 

지금부터 index를 빼고, detail, results, vote 페이지를 추가 작성 해 보겠다. 
모든 페이지: index, detail, results, vote
추가할 페이지: detail, results, vote

### 1. 페이지를 추가하기 전 polls/views.py와 urls.py

* polls/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! ")
```
<br>
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

### 2. page를 추가한 후 views.py와 urls.py

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
<br>
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
<br>
* 화면
* `http://localhost:8000/polls`

```
Hello, world!
```
<br>
* `http://localhost:8000/polls/detail`

```
detail page using HttpResponse
```
<br>
* `http://localhost:8000/polls/results/`

```
response page using valiable and HttpResponse.
```
<br>
* `http://localhost:8000/polls/vote/`

```
vote page using HttpResponse
```

### 3. request외 파라미터 추가 

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
<br>
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
<br>
* 화면
* `http://localhost:8000/polls/1/`

```
You're looking at question 1.

# 만약 http://localhost:8000/polls/2/
# You're looking at question 2.
```
<br>
* `http://localhost:8000/polls/2/results/`

```
Yor're looking at the results of question 2.
```
<br>
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
<br>
<br>
<br>


### View가 할 수 있는 것들

<hr>

* 각 view는 요청된 페이지의 내용이 담긴 HttpResponse객체를 반환하거나,  Http404 같은 예외를 발생하게 한다.
* <span style="color:tomato">자유롭게</span> view가 어떤 행동을 하도록 할 수 있다. 
* 데이터베이스의 레코드를 읽을 수도 있다.
* Django나 python에서 서드파티로 제공되는 태플릿 시스템을 사용할 수 있다. 
* PDF를 생성하거나, XML 출력을 하거나, 실시간으로 ZIP 파일을 만들 수 있다. 
* view는 원하는 무엇이든, Python의 어떤 라이브러리던 사용할 수 있다. 
* .....

<p style="color:tomato">모든 Django는 <u>HttpResponse</u>객체나, 혹은 <u>예외(execption)</u>을 원한다.</p>

<br>
<br>
<br>

### 코드와 디자인을 분리, index.html

<hr>

view에서 <u>페이지의 디자인이 하드코딩</u> 되어있다면 문제가 생긴다.  만약 페이지가 보여지는 방식을 바꾸고 싶다면, python코드를 편집해야하는데.. 

이때, <span style="color:tomato"> view가 사용할 수 있는 탬플릿을 작성 </span>하여, <span style="color:tomato"> Python 코드로부터 디자인을 분리 </span>하도록 Django의 탬플릿 시스템을 사용해 볼 것이다. 

>1. view가 사용할 수 있는 탬플릿 작성
>2. python 코드로 부터 디자인을 분리
<br>

* polls/views.py 에 추가 
  <p style="color:grey">polls/views.py페이지에 하드코드 되어 있는 상태</p>

```python
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```
<br>

* 화면 

```
b_question, a_question
```
<br>


<br>
* polls/templates/polls/index.html
  <p style="color:grey"> 탬플릿에 코드 입력</p>

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
<br>
* polls/views.py
  <p style="color:grey"> template을 이용하여 polls/views.py에 index view를 업데이트</p>

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
<br>
* 화면

```python
* b_question
* a_question
```

<p style="color:grey"> **[question]** Django 탬플릿을 사용할 때는 무조건 HttpResponse(template.render(context, request))가 되어야 하는 걸까? </p>
<br>
<br>
<details>
<summary><strong>하드코딩에서 Django 탬플릿 시스템 사용을 사용하기 위한 <u>코드 편집</u></strong></summary>
<br>
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

### 4. 지름길: render()
`template`에 **context**를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법이다. 따라서 Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능`shortcuts`을 제공

* polls/views.py
  index() view를 단축 기능으로 작성하기

```python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

```
> 모든 view에 적용한다면, 더 이상 loader와 HttpResponse를 import하지 않아도 된다. 
> render()함수는 request객체를 첫번째 인수로 받고, template 이름을 두번째 인수로 받으며, context 사전형 객체를 세번째 선택적 (optional)인수로 받는다. 
> 인수로 지정된 context로 표현된 templte의 HttpResponse객체가 반환된다.

* **render()함수의 인수**
```
(request, template, context(optional))
```
</details>
<br>
<br>
<br>

### 404에러 

<hr>

detail view에서는 지정된 설문조사의 질문 내용을 보여준다. 

* polls/views.py
  view는 요청된 질문의 ID가 없을 경우, Http404예외를 발생시킨다.

다음 구문을 추가
```python
from django.http import Http404

def detail(request, question_id):
    try:
        question = Question.obejcts.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

```
* polls/template/polls/detail.html

```python
{{question}}
```
<br>
<br>
<details>
<summary><strong>예외처리의 다른 방법</strong></summary>
<br>
quesiton_id가 없을 경우, **예외처리**를 띄워주어야 한다. 따라서 question_id가 없는 경우는 404에러를 일으키도록 명령한다. 

에러를 일으키는 방법에는 여러길이 있다. 

### 1. 404에러 일으키기 1, get()

만약 객체가 존재하지 않을 때 **get()**을 사용하여 Http404예외를 발생시키는 것은 자주 쓰이는 용법이다. 

<br>
* polls/views.py

```python
from django.http import Http404

from django.shortcuts import render
from .models import Question

def detail(request, question_id):
    # question_id가 있는 경우
    try:
        question = Question.objects.get(pk=question_id)
    # question_id가 없는 경우
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls.detail.html', {'question': question})
```
<br>
* polls/templates/polls/detail.html

```html
{{question}}
```
<br>
* 화면

> ```
> a.question
> b.question
> ```
>
> a.question을 클릭하면 a.question이라는 문구가 나온다. 

### 2. 404 에러 일으키기 2, get_object_or_404() 

객체가 존재하지 않을 때 get()을 사용해서 Http404예외를 발생시킬 수도 있다는 것을 알았다.

하지만 Django에서는 단축 기능을 제공하고 있기도 하다. 

**get_object_or_404()** 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get()함수에 넘긴다. 만약 객체가 존재하지 않을 경우, Http404예외를 발생시킨다.
<br>
* polls/views.py

```python
from django.shortcuts import get_object_or_404, render
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
```

**get_list_or_404()** 함수는 get()대신 filter()를 쓴다는 것이 다르다. 리스트가 비어있을 경우, Http404예외를 발생시킨다.

</details>
<br>
<br>
<br>

### Template 시스템 활용, 코드와 디자인을 분리, detail, results, vote
<hr>

<strong> context 변수 question이 주어졌을 때, <br>
polls/detail.html라는 template이 어떻게 될까?</strong>
<br>
* polls/templates/polls/detail.html

```python
<h1>{{question.question_text}}</h1>
<ul>
{% for choice in question.choice_set.all%}
	<li>{{choice.choice_text}}</li>
{% endfor %}
</ul>
```

> template시스템은 <u>변수의 속성에 접근하기 위해</u> 점-탐색(dot-lookup)문법을 사용한다.
>
> ```html
> {{question.question_text}}
> ```
>
> - question객체에 대해 사전형으로 탐색한다.
> - 탐색에 실패하면 속성값으로 탐색한다.
> - 속성탐색에도 실패하면 리스트의 인덱스 탐색을 시도한다.

<br>
<br>
<br>

### template에서 하드코딩된 URL 제거

<hr>

polls/index.html template에 링크를 적으면, 이 링크는 부분적으로 하드코딩된다.

```python
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

하지만 **강력하게 결합된 하드코딩**된 접근방식의 문제는 수 많은 탬플릿을 가진 프로젝트들의 URL의 변경을 어렵게 한다. <br>
<span style="color:red"> {% url %} template 태그</span> 를 사용한다. 이 태그를 사용하면 url설정에 정의된 특정한 URL 경로들의 `의존성`을 제거할 수 있다. 

* <a href="http://smiler.tistory.com/entry/%EB%86%92%EC%9D%80-%EC%9D%91%EC%A7%91%EB%8F%84%EC%99%80-%EB%82%AE%EC%9D%80-%EA%B2%B0%ED%95%A9%EB%8F%84">의존성</a>: 낮은 결합도를 가진 프로그램 코드는 한 모듈 내의 에러가 다른 모듈에 영향을 미치는 파급효과의 최소화가 가능하며, 한 모듈의 변경이 다른 모듈에 큰 영향을 미치지 않고 모듈의 유지 보수 및 변경이 가능하다. 

출처: [http://smiler.tistory.com/entry/높은-응집도와-낮은-결합도](http://smiler.tistory.com/entry/%EB%86%92%EC%9D%80-%EC%9D%91%EC%A7%91%EB%8F%84%EC%99%80-%EB%82%AE%EC%9D%80-%EA%B2%B0%ED%95%A9%EB%8F%84) [아직은 내가 쓴 글보다 퍼온 글이 훨씬 많음]

<br>

<br>

<details>

<summary><strong>url 관련해서 결합도 낮추기</strong></summary>

### 1. 강력하게 결합된 하드코딩된 접근방식을 바꾼다.

* polls/index.html

하드코딩되어있는 URL링크

```python
 <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```
<br>
* polls/index.html

{% url %} 태그로 하드코딩된 코드를 바꿔준다.

```python
<li><a href="{% url 'detail' question.id %}">{{question.question_text}}</a></li>
```

polls/ulrs모듈에 서술된 URL의 정의를 탐색하는 식으로 동작한다. 'detail'이라는 이름의 URL이 어떻게 정의되어 있는지 확인할 수 있다. 

> 만약 URL을 바꾸고 싶다면, 
> polls/specifics/12/
> polls/urls.py에서 바꿔준다.
>
> ```python
> path('specifics/<int:question_id>', views.detail, name='detail'),
> ```



### 2. App이 여러개일 때  URL 구별

* Django project는 app이 몇개라도 올 수 있다. 
* 같은 project에 위치한 app들의 url 구별

URLconf에 이름공간(namespace)를 추가

polls/urls.py파일에 app_name을 추가하여 어플리케이션의 이름공간을 설정한다. 
<br>
* polls/urls.py

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
<br>
* polls/index.html template

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

app name을 추가하도록 한다.

```python
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```



</details>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Django

## Form

view 추가를 무사히 마쳤다. 
따라서 form 만들기를 계속해서 진행!

주된 참고 페이지: [첫 번째 장고 앱 작성하기, part4](https://docs.djangoproject.com/ko/2.0/intro/tutorial04/)
<br>
<br>
<br>

### 간단한 폼 만들기

<hr>

* polls/templates/polls/detail.html

```python
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action=" {% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{forloop.couter}}" value="{{ choice.id }}"/>
    <label for="choice{{forloop.couter}}">{{choice.choice_text}}</label><br/>
{% endfor %}
<input type="submit" value="vote"/>
</form>
```

<span style="color:grey">아직 어떤식으로 작동하는지 잘 모르겠.. </span>
<br>
<br>
<br>
<br>
<br>

### vote method 구현

<hr>

* polls/views.py

```python
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render


def vote(request, question_id):
    # vote 함수 구현
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
```

