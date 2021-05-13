use std::io;

fn main() {
    println!("Guess the Num");
    println!("type your answer:");

    let mut guess = String::new();

    io::stdin().read_line(&mut guess).expect("can't read");

    println!("your answer: {}",guess);
}
