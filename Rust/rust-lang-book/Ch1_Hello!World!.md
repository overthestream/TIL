# 시작하기

## Reference

러스트 프로그래밍 공식 가이드

## 1.1 설치하기

### macOS rustup 설치

```sh
$ curl https://sh.rustup.rs -sSf | sh
```

터미널 다시 로그인 시 컴파일러를 PATH에 등록.

만약 곧바로 등록하려면

```sh
$ source $HOME/.cargo/env
```

### update/remove

```sh
$ rustup update
$ rustup self uninstall
```

### version
```sh
$ rustc --version
```

### local docs
```sh
$ rustup doc
```

## 1.2 첫번째 러스트 프로그램 작성하기

``` rs
fn main(){
  println!("Hello, World!);
}
```
```sh
$ rustc hello_world.rs # 컴파일
$ ./hello_world # 실행 파일 실행
```

fn main() : 매개 변수, 리턴 값이 없는 main 함수 선언

println! : 러스트 매크로. 

!는 함수가 아니라 매크로를 호출한다.

## 1.3 카고 알아보기 

빌드, 라이브러리 의존성 등 관리 