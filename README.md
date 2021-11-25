# Final PJT



### 1. 프로젝트 컨셉

------

* 장르 기반의 추천 서비스

* 유저가 보고 평점을 남긴 영화를 기준으로 장르를 선정

* 유저의 데이터가 부족할 경우(평점을 매긴 영화의 갯수 10개 미만) 랜덤한 영화들을 추천



### 2. 구조 및 사용 기술

------

- Django를 사용하여 서버를 구성
- Django의 ORM을 활용하여 데이터베이스를 관리
- JavaScript에서 axios를 활용하여 검색 및 페이지 이동시 페이지 리로드를 하지 않고 QuerySet을 받아 부분적으로 갱신함



### 3. 팀원 및 역할 분담

------

팀장 : 윤홍림 - Front / Django, html, css

팀원 : 우윤석 - Back / Django, Algorithm, JavaScript, html



### 4. 데이터베이스 모델링(ERD)

------

![image-20211125145602533](../../assets/images/README/image-20211125145602533.png)

* 평점을 TMDB에서 가져오지 않고 404 Movies사이트 유저들 끼리의 평점을 매길 수 있도록 user와 movie를 M:N관계로 설정 through를 통해 중개모델인 Rates를 만들어서 평점을 관리할 수 있게 했다.
* 유저:게시글, 유저:댓글, 게시글:댓글 관계는 1:N으로 설정했다.
* 영화 하나에 여러장르가 포함될 수 있고 하나의 장르에 여러 영화가 있기 때문에 M:N관계로 설정

### 5. DATABASE

------

- TMDB의 API를 사용

- TMDB의 API 중 Top Rated데이터를 50페이지까지 활용

- TMDB의 Genres data 또한 참고하여 활용
- update.py 실행 시 해당 API에서 영화 데이터를 가져와서 movie.json에 저장
- python manage.py loaddata ./movie/fixtures/movie.json 명령어 실행



### 6-1. USER

------

- 회원가입, 로그인, 로그아웃 기능 구현
  - AbstractUser모델을 상속받아 사용

- 회원 가입 기능 : CustomForm을 사용하여 회원가입할 때 필요한 부분만 출력되도록 변경
- 로그인 기능 : Bootstrap Form을 사용하여 꾸밈
- 로그인, 로그아웃, 회원가입 버튼
  - 로그인, 회원가입, 로그아웃 버튼은 어느 페이지에서도 볼 수 있도록 상단 NavBar에 배치하였다.



### 6-2. COMMUNITY

------

- 유저들이 게시글과 댓글을 통해 소통을 나누는 공간
- 영화 정보 사이트이니 영화 스크린샷 업로드가 가능하도록 이미지 첨부도 가능하게 했다.
- Board
  - 커뮤니티 메인화면에서 사람들이 쓴 게시글들을 보기 편하게 Table로 만들어서 정리했다.
  - 작성자, 제목, 작성날짜 어디를 클릭하던 그 글이 작성된 detail로 넘어가게 해놓았고, 로그인한 유저라면 새글 작성이 가능하게 해놓았다.

- Detail
  - 게시글을 눌러 들어올 시 내용이 보이고 작성자인 경우 수정, 삭제가 가능하게 만들었다.
  - 댓글은 로그인한 유저라면 작성 가능하게 만들었고, 작성한 유저 본인이면 댓글을 삭제 가능하게 만들었다.

### 6-3. MOVIE

------

- 영화의 평점이 0점인 경우는 아무도 평점을 매기지 않았다는 의미이므로 평점표기 대신 평점이 매겨지지 않았다고 표시를 해주었다.
- Home 화면
  - JS를 사용하여 360도로 회전하는 이미지 슬라이드를 이용하여 슬라이드로 볼 수 있게 만들었다. 무작위 영화 10개의 포스터 정보를 Django 서버와 Axios통신을 통해서 불러왔다.
- 영화 추천 화면
  - 로그인한 유저가 평점을 등록한 영화가 10개 이상일 경우 가장 많이 본 장르를 추천해준다
  - 평점을 등록한 영화가 10개가 안될 경우 무작위로 추천해서 보여준다.
- 키워드 검색
  - 키워드를 입력하면, 해당 키워드가 줄거리나 제목에 있는 영화들을 출력하여 보여줍니다.
  - 검색 버튼을 누를 경우 리로딩을 하지 않고 Axios통신을 통해 QuerySet을 받아와서 HTML에 추가해줘서 부분적 새로고침을 사용해 페이지네이션 까지 구현하였다.
- 장르 검색
  - Bootstrap의 NavBar Dropdown 메뉴를 이용하여 genre.json에 있는 모든 장르를 보여준다.
  - 장르 하나를 골라서 클릭하면 해당 장르의 영화를 모두 보여준다.
  - Pagination을 이용하여 한 페이지에 10개의영화가 보여지고, 페이지 이동이 가능하다.
- Detail 하면
  - 해당 영화의 영화 포스터와 제목, 장르, 줄거리, 평점이 출력되고, 로그인한 유저라면 해당 영화의 평점을 등록할 수 있습니다. 
  - Axios통신을 통해 평점을 변경하면 바로 변경된 사항이 적용될 수 있도록 했습니다.
  - 평점 적용 및 수정 시 해당 영화의 평점을 서버에서 계산해서 갱신하도록 했습니다.
  - 장르는 태그화 하여 해당 장르를 클릭하면 장르검색에서 클릭한 것처럼 해당 장르의 영화들을 출력하는 페이지로 넘어갑니다.



### 6-4. NavBar

------

- NavBar는 2개가 적용되었다.
  - 최상단 NavBar는 영화 사이트의 이름과 아이콘이 왼쪽에 배치되게 하였고, 오른쪽에는 로그인 한 유저라면 로그아웃 버튼이, 로그인하지 않은 유저라면 로그인 버튼과 회원가입 버튼이 출력되게 되어있다.
  - 그 밑의 NavBar는 Home, 커뮤니티, 영화 추천, 키워드 검색, 장르 검색에 해당하는 부분으로 클릭하면 넘어갈 수 있게 만들었다.





### 발전시킬 만한 부분들

------

- 일단 데이터 자체가 많지 않기 때문에 사용자의 데이터가 부족할 경우 랜덤 영화를 추천하도록 되어있지만 평점순으로 영화를 추천하는것도 좋은 방법일 것이라고 생각

- 장르검색의 경우 페이지네이터를 javascript로 구현하지 않아서 페이지 전체 리로딩이 된다. 이부분 개선

- Home화면에서 마우스 커서 형태가 grab으로 설정되어 있어서 이미지에 a태그를 통해 하이퍼링크를 넣었지만 그림 클릭을 해도 해당 영화 디테일로 넘어가지 않는다. 이 부분 해결 필요

- 그 외 더 다양한 기능들 추가

  

### 데이터베이스 업데이트 하는 방법

```
python update.py
python manage.py loaddata ./movie/fixtures/genres.json
python manage.py loaddata ./movie/fixtures/movie.json 
```

