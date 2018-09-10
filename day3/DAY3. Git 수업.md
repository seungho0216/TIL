# DAY3. Git 수업

## 1. Git 기본

### 1)

### 2)

### 3)

## 2. Git 복구

### 1)

### 2)

### 3) checkout 으로 복구하기

#### 	1. 실수로 파일을 잘못 수정 후 commit 시킨 경우

#### 	2. git log로 SHA 확인 (d5d1ab7086d1fbaf87680a8e8519beccede5b7b1 처럼 생김)

#### 		3. git checkout  SHA앞4자리 

#### 	4. 임시적으로 복원됨

#### 	5. 잘못 수정한 부분에서 파일로 들어가 복사 후 클립보드로 복사

#### 	6. git checkout master 로 돌아가 파일에 붙여넣기 후 저장 

#### 	7. git add . 그리고 git commit -m "메세지"로 수정 커밋





# 3. Faker 모듈

## 1) Python 3 에서 faker 모듈 사용하기

#### 1. $ sudo pip3 install faker 로 faker 모듈 설치

#### 2.  .py 파일 에 faker모듈 import 시키기

  - `from faker import Faker`

#### 3. 함수 정의 시키기

- `@app.route("/ffaker")
  def ffaker():
      name = fake.name()
      address = fake.address()
      job = fake.job()
      return render_template('ffaker.html', name=name, address=address, job=job)`

#### 4. ffaker.html 파일 생성

- <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Faker 모듈</title>
  </head>
  <body>
      <h1>뭡니까</h1>
      <h1>{{ name }}</h1>
      <h2> {{ address }}</h2>
      <h3> {{ job }}</h3>
  </body>
  </html>



#### 5. 끝















