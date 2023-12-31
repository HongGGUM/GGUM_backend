## 서버

- [생성한 가상 서버 (인스턴스)](https://www.notion.so/AWS-41624ac80d6242a29014fd66840a1abd?pvs=21)
- aws 계정
    - 아이디 : [hyejin2371@gmail.com](mailto:hyejin2371@gmail.com)
    - 비밀번호 : phj9192371@
- 인스턴스ID : i-0f8845ec796d87044
- 서버 주소 :  [http://172.31.40.88:5000](http://172.31.40.88:5000/)

# DB

1. [인스턴스 세팅](https://velog.io/@kyj311/AWS-EC2-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)
2. [RDS (Relative Database Service) 인스턴스 생성](https://velog.io/@kyj311/AWS-RDS-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)
3. 생성한 DB 인스턴스 정보 : [링크](https://ap-northeast-2.console.aws.amazon.com/rds/home?region=ap-northeast-2#database:id=honggumdb;is-cluster=false) 에서 직접 확인 가능
    1. 마스터 암호 : hongik45
    2. 마스터 사용자 이름 admin
    3. DB 인스턴스 식별자 (이름) : honggumDB
    4. 포트 : 3306
    5. host (엔드포인트) : honggumdb.capnwelofgc3.ap-northeast-2.rds.amazonaws.com



# user
### '/users'
```
[GET] login() 
{
	student_number : 
	password:
}
```
```
 [POST] sign_in()
{
	name:
	student_number : 
	cohort:
	password:
}
  
```
# diary
### '/diaries/ { string : date }'
```
[GET]  해당 날짜에 등록된 diary 의 {id, title, user_name} 을 반환
return {
                "diary_id" : id,
                "title" : title,
                "user_name" : user_name,
            }
```
```
[POST] new_diary 를 DB에 추가하고 새로 생성한 diary의 id를 반환

request {
	user_id :
	title:
	content:
}
return {
            "message": "diary created successfully",
            "diary_id": new_diary_id
        }
```
  
### '/diaries/ { string : date }/{ int : user_id }'
```
[PUT] 특정 날짜에 특정 사용자가 작성한 diary 내용을 수정
request {
	id: #수정할 diary 선택
	user_id: #작성자만 수졍 가능하도록
	title:
	content:
}
return{
            "message": "update successfully",
            }
```
```
[DELETE]  특정 날짜에 특정 사용자가 작성한 diary를 삭제
return {
            'msg': 'data deleted successfully'
            }
```
  
# notice
### '/notices'
[GET] 최근 n개 공지를 반환, , http://127.0.0.1:5000/notice?count=n 꼴로 요청
```
[POST]
request {
	user_id: 
	title :
	content :
}
return {
        "notice_id": notice_id
    }
```
  
### '/notices/{ int : notice_id }'
```
[PUT]
request {
	user_id : # 작성자만 수정 가능하도록 확인 위함 
	title : 
	content :
}
	#last_edit_at 업데이트 필요

return{
	'msg' : '사용자가 일치하지 않습니다 / 수정 성공'
}
```
```
[DELETE]
request {
	user_id: #작성자만 삭제 가능하도록 확인
}
return{
	'msg' : '사용자가 일치하지 않습니다 / 삭제 성공'
}
```
  
# survey
### '/surveys'
```
[POST]
request {
        'survey_date':
        'user_id':
        'title': 
        'description'
}
return {
        'msg': msg,
        'id': new_id
    }
```
```
[GET] 활성화중인 survey를 로드
return {
        'id' 리스트
}
```

### '/surveys/ { int : survey_id }'
```
[GET] 해당 survey의 정보를 로드
return {
        'survey date': date,
        'title': title,
        'desc': desc,
    }
```

```
[PUT] 투표 게시글 수정
request{
        'survey_date':
        'user_id':
        'title': 
        'description'
        'isactive'
중 수정 원하는 항목
}
```

```
[DELETE] 투표 게시글 삭제
request {
        'user_id':
}
```
  

### '/surveys/ { int : survey_id } /participant'
```
[POST] survey에 attendee 등록
request { 'attendee_id' }
return { 'msg' } 

[GET ] 해당 survey에 참석한 attendee를 로드
{ id 리스트}

[DELETE] 투표취소
request { 'attendee_id' }
return { 'msg' } 
```
