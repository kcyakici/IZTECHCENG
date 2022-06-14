#lang scheme

(define check_if_even
  (lambda (x)
  (if (even? x)
      x
      (- x 1)
      )))

(define sum_of_even_integers
  (lambda (n)
  (if (= (check_if_even n) 2) ; assuming the user don't enter something less than 2
      2
      (+ (check_if_even n) (sum_of_even_integers (- n 2)))
         )))

(sum_of_even_integers 6) ; Example call 1
(sum_of_even_integers 7) ; Example call 2