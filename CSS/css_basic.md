## CSS

#### Inline (인라인)

- HTML 요소의 style에 CSS 넣기

<br>

#### Embedding (내부 참조)

- HTML 내부에 CSS 넣디

<br>

#### link File (외부 참조)

- 외부에 있는 CSS 파일을 로드하기
- 컴포넌트 화 

<br>

<br>

#### 박스 모델의 구성

- Content
- Padding
  - 상하좌우
- Margin
  - 상하좌우
- Border
  - 상하좌우

- shorthand
  - 다양한 shortcut 활용도 가능하다.
    - 1개 : 
    - 2개 : 
    - 3개 : 
    - 4개 : 시계방향으로 적용

<br>

<br>

#### display 속성

##### block

- 항상 새로운 라인에서 시작

- 화면 크기 전체의 가로폭을 차지한다. (기본적으로 너비의 100%)

  - margin-right : auto

    - 나머지 빈 곳을 margin  -> 왼쪽 정렬

  - margin-left: auto

    - 나머지 빈 곳을 margin  -> 오른쪽 정렬

  - margin-right : auto

    margin-left: auto

    - 가운데 정렬

<br>

##### inline

- 새로운 라인에서 시작하지 않으며 문장의 중간에 들어간다.
- content의 너비 만큼 가로폭을 치지한다.

<br>

##### inline-block

- block과 inline 레벨 요소의 특징을 모두 갖는다.

<br>

##### none

- 해당 요소를 화면에 표시하지 않는다. (공간조차 사라짐)

<br>

##### display  : none VS visibility : hidden

- none : 보이지도 않고 공간도 차지하지 않는다.
- hidden : 보이진 않지만 공간은 차지한다.

<br>

<br>

#### Position 

##### static

- 기본적인 요소의 배치 순서에 따라 위 -> 아래, 왼쪽 -> 오른쪽으로 순서에 따라 배치된다.

- 부모 요소의 위치를 기준으로 배치된다.

<br>

##### relative

- 기본 위치를 기준으로 좌표 프로퍼티 (top, bottom, left, right) 를 사용하여 위치를 이동한다.
- 음수도 가능하다.

<br>

##### absolute

- 부모 요소 또는 가장 가까이 있는 조상 요소를 기준으로 좌표 프로퍼티 (top, bottom, left, right)만큼 이동한다. 

<br>

##### fixed

- 부모 요소와 관계없이 브라우저의 viewport를 기준으로  좌표 프로퍼티 (top, bottom, left, right)를 사용하여 위치를 이동시킨다. 

<br>