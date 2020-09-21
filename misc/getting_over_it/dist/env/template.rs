fn sandbox(x: &mut u64) {
    /* code */
    *x += 1;
    sandbox(x);
}

fn main() {
    let mut cnt = 0;
    sandbox(&mut cnt);
    println!("{} loops. Good job!", cnt);
    println!("Flag is TSGLIVE{{/* redacted */}}");
}
