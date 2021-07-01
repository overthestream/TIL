# 마크다운

<hr/>

## 마크다운이란?

텍스트 기반의 마크업 언어

HTML로 변환이 가능

간결하고 다양하게 작성 가능

단, 표준이 없다

<hr/>

## 문법

### - 제목(Header)

"#"의 개수 : HTML의 h1~h6 태그와 동일(6개까지만 가능)

    # this is H1
    ## this is H2
    ### this is H3
    #### this is H4
    ##### this is H5
    ###### this is H6
    ####### this is H7

# this is H1

## this is H2

### this is H3

#### this is H4

##### this is H5

###### this is H6

####### this is H7

<hr />

### - 인용(BlockQuote)

">"문자 사용, 탭으로 중복 가능

    > first
    >   > second
    >   >   > third

> first
>
> > second
> >
> > > third

<hr/>

### - 목록

순서 있는 목록

    1. 첫번째
    2. 두번째
    3. 세번째

1. 첫번째
2. 두번째
3. 세번째

순서 없는 목록(\*, +, -, 혼합 가능)

    * 첫번째
      * 두번째
        * 세번째
    + 첫번째
      +두번째
        + 세번째
    - 첫번째
      * 두번째
        + 세번째

- 첫번째
  - 두번째
    - 세번째

* 첫번째
  - 두번째
    - 세번째

- 첫번째
  - 두번째
    - 세번째

<hr/>

### - 코드

4개의 공백(탭) + 한 줄 개행해야 함

    normal
        code

normal

    code


또는 backtic 3개

    ```Hello! World!```

```
Hello! World!
```

또는

inline code

    <pre><code>{Hello! World!}</code></pre>

<pre><code>{Hello! World!}</code></pre>

또는 
backtic 1개 


<hr/>

### - 구분선

    <hr/>

<hr/>

### - 링크

- 참조 링크

      [link keyword][id]

      [id]: URL "Optional Title here"

      // code
      Link: [Google][googlelink]

      [googlelink]: https://google.com "Go google"

  [link keyword][id]

  [id]: URL "Optional Title here"

  // code
  Link: [Google][googlelink]

  [googlelink]: https://google.com "Go google"

- 외부 링크

      사용문법: [Title](link)
      적용예: [Google](https://google.com, "google link")

  사용문법: [Title](link)
  적용예: [Google](https://google.com, "google link")

- 자동 연결

      일반적인 URL 혹은 이메일주소인 경우 적절한 형식으로 링크를 형성한다.

      * 외부링크: <http://example.com/>
      * 이메일링크: <address@example.com>

  일반적인 URL 혹은 이메일주소인 경우 적절한 형식으로 링크를 형성한다.

  - 외부링크: <http://example.com/>
  - 이메일링크: <address@example.com>

<hr/>

### - 강조

    *single asterisks*
    _single underscores_
    **double asterisks**
    __double underscores__
    ~~cancelline~~

_single asterisks_
_single underscores_
**double asterisks**
**double underscores**
~~cancelline~~

<hr/>

### - 이미지

    ![Alt text](/path/to/img.jpg)
    ![Alt text](/path/to/img.jpg "Optional title")

HTML 태그 달듯이 써서 속성 조절 가능

    <img src="/path/to/img.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
