is_prerequisite(X, Y) :- prerequisite(X, Y). % left predicate, rule as a whole
is_prerequisite(X, Y) :- prerequisite(X, Z), is_prerequisite(Z, Y).

is_four_credit(X) :- credit(X, 4).
is_three_credit(X) :- course_core(X), \+ credit(X, 4).
is_three_credit(X) :- course_elective(X), \+ credit(X, 4). % instead of writing all the three credit courses one by one, we can just check whether the course is four credit and if it is not, we can conclude that it is a three credit course.

prerequisite(ceng112, ceng113). % facts
prerequisite(ceng211, ceng113). 
prerequisite(ceng311, ceng214).
prerequisite(ceng415, ceng316).
prerequisite(ceng424, ceng415). % because of transitivity, ?-prerequisite(ceng424, ceng316). must also return "true" because one cannot take ceng424 course without taking ceng316 first. In addition, ?-is_prerequisite(X, Y) must return both X = ceng424 Y = ceng415 and X = ceng424 Y = ceng316
 
credit(math141, 4). % facts
credit(phys121, 4).
credit(ceng113, 4).
credit(math142, 4).
credit(phys122, 4).
credit(ceng215, 4).
credit(math255, 4).
credit(ceng214, 4).
credit(ceng311, 4).
credit(math322, 4).

course_core(ceng111).
course_core(ceng113).
course_core(ceng115).
course_core(ceng112).
course_core(ceng211).
course_core(ceng213).
course_core(ceng215).
course_core(ceng212).
course_core(ceng214).
course_core(ceng216).
course_core(ceng218).
course_core(ceng222).
course_core(ceng311).
course_core(ceng315).
course_core(ceng323).
course_core(ceng312).
course_core(ceng316).
course_core(ceng318).
course_core(ceng322).
course_core(ceng411).
course_core(ceng415).
course_core(ceng400).
course_core(ceng416).
course_core(ceng418).
course_core(ceng424).
course_core(math141).
course_core(phys121).
course_core(eng101).
course_core(math142).
course_core(phys122).
course_core(math144).
course_core(eng102).
course_core(math255).
course_core(hist201).
course_core(turk201).
course_core(hist202).
course_core(turk202).

course_elective(ceng381).
course_elective(ceng382).
course_elective(ceng383).
course_elective(ceng384).
course_elective(ceng386).
course_elective(ceng388).
course_elective(ceng389).
course_elective(ceng390).
course_elective(ceng391).

teaches(mustafa_ozuysal, ceng216).
teaches(burak_galip_aslan, ceng214).
teaches(selma_tekir, ceng213).
teaches(turgut_kalfaoglu, ceng312).
teaches(serap_sahin, ceng322).
teaches(mustafa_ozuysal, ceng216).
teaches(berat_alper_erol, ceng424).
teaches(nesli_erdogmus, ceng463).
teaches(damla_oguz, ceng435).
teaches(isil_oz, ceng311).