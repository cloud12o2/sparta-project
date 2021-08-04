# Which Movie
최신 영화 정보 및 개봉예정작을 한번에 볼 수 있고, 해당 영화를 검색 할 수 있는 사이트입니다. <br/>
네이버 API를 사용해 검색 기능을 구현했고 다양한 사이트에서 영화 관련 정보를 크롤링해서 보여주고 있습니다. <br/>
추가적으로 게시판에서 영화에 대한 정보 및 리뷰를 작성 할 수도 있습니다.


<a href="http://whichmovie.shop/">Which Movie 링크로 가기</a> <br/>

![썸네일](https://user-images.githubusercontent.com/70641418/127768727-74e0a62f-9d35-4e1f-89a1-3bb7fb8b2084.JPG)


<br/>
<br/>


## 팀원

- Front-end: 이아람, 방하은
- Back-end: 김남운, 임전혁

<br/>

## 개발기간
기간: 2021.07.19 ~ 2021.07.29 (11일)  
<br/>

## 적용기술  
  
- Front-end: HTML, CSS, JavaScript, Jquery, Flask, Jinja2
- Back-end: Python, Flask, Jinja2, MogoDB

<br/>

## 구현 기능

### Front-end
1. 네이버 검색 API를 활용한 영화 검색
2. 네이버 검색 API 사용 시 Ajax 활용
3. Pagination 및 영화 순위 슬라이드 기능 구현 시 JS와 Jquery 사용

### Back-end
1. Beautiful Soup을 활용한 영화 순위 및 개봉예정작 크롤링
2. 크롤링한 데이터 NoSQL인 MogoDB를 활용 insert
3. 게시판 페이지에서 CRUD 기능 구현

<br/>
<br/>

## 개인 역할

<code>임전혁</code>
1. 팀장 역할 및 협업을 위한 깃 환경설정
2. 웹 크롤링을 활용한 영화관련 데이터 수집
3. 수집한 데이터 페이지에 출력 및 정제

<code>김남운</code>
1. 개봉예정작 페이지에 들어갈 영화리스트를 yes24, 다음, 왓차등의 영화관련 웹사이트에서 크롤링
2. 직접 크롤링한 데이터를 데이터베이스에 insert
3. insert한 데이터를 Jinja2 반복문 문법을 사용해서 화면에 출력


<code>이아람</code>
1. 메인페이지 와이어프레임 제작
2. 네비게이션, 푸터 제작
3. 개봉예정작 페이지 제작 - 좋아요(하트) 기능    
  Javascript mouseenter사용하여 좋아요 클릭 구현
4. 게시판 메인, 작성 페이지 제작

<code>방하은</code>
1. 메인페이지를 담당, 반응형 페이지 구현
2. Python, Javascript Ajax 활용하여 네이버 영화검색 오픈 API 를 호출, 영화 검색창 기능 구현
3. 한 페이지에 최대 10개까지 보여지는 검색 결과창 구현
4. 영화 검색 결과 갯수에 따라 페이지가 붙고, 다음 페이지를 누를 경우 다음 10개의 검색결과가 새로 붙는 Pagination 구현
5. 영화 추천 컨텐츠 - Css 호버링 기능으로 마우스를 올렸을 때 이미지가 커지는 애니메이션 구현



## 소감 및 후기

<code>임전혁</code>
- 처음 팀프로젝트를 진행하면서 팀장 열학을 맞아봤습니다.   
부족한 점이 많았지만, 팀원분들이 적극적으로 참여해주셔서 재미있게 프로젝트를 진행 했습니다.    
프로젝트를 진행하면서 아이디어 구상부터 그 아이디어를 바탕으로 구현 하면서 막히는 부분이 많았습니다.   
하지만 그만큼 배우는 것도 정말 많았던 것 같습니다.   
다음에도 팀프로젝트를 진행 한다면 더욱 좋은 결과물을 얻을 수 있을거라 생각합니다.   

<code>김남운</code>
- 내가 코딩을 하다니 너무 놀랍다.<br/>
생각보다 고민 하는 과정이 고통스럽지만 즐거운것도 놀라웠다.<br/>
혼자하면 버거웠을 프로젝트가 모든 팀원들의 기여로 빠르고 성공적으로 끝나 기쁘다.<br/>
개발에 대한 흥미를 깨운 좋은 시작이었고, 앞으로의 배움이 기다려지게된 프로젝트였다.<br/>
빨리 더 배우고싶다 !!!   

<code>이아람</code>
- 처음 하는 팀프로젝트에서 어려운 부분도 많았고 처음 사용하는 git.. 때문에 애먹기도 했지만,    
11일이라는 짧은 기간임에도 각자 맡은 포지션에서 열심히 해주신 덕에 잘 끝낼 수 있었습니다.   
프로젝트를 하면서 좀 더 열심히 공부해야겠다는 동기부여도 받았습니다.   
팀 프로젝트로 의견을 주고 받으며 만들어낸 결과물을 보면서 혼자서 공부하는 것보다 훨씬 좋은 경험을 되었습니다.   
좋은 사람들과 좋은 경험을 하게되어서 보람있는 11일을 보냈습니다.   
모두 고생많으셨습니다!


<code>방하은</code>
- 코딩 공부 한 달 차에 처음 진행해보는 프로젝트라 어렵고 막막했지만, <br/> 
각자의 분야에서 열심히 노력하는 팀원들 덕분에 프로젝트를 잘 마무리할 수 있었던 것 같습니다.<br/>
코딩이란 배운 것에 국한된 것이 아니라 내가 직접 찾아 알아내야한다는 말을 깨닫게 되는 11일이였습니다.<br/>
모두 감사드립니다!
