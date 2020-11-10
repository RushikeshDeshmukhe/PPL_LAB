
# Top of tree is coep years i.e this is for 2nd year
# Also for perticular department CS

coep_year(coep,1). 
coep_year(coep,2). 
coep_year(coep,3). 
coep_year(coep,4). 

year_dept(2,comp).
year_dept(2,entc).
year_dept(2,electrical).
year_dept(2,civil).
year_dept(2,mechanical).

dept_subj(comp,dsa).
dept_subj(comp,odemc).
dept_subj(comp,ppl).
dept_subj(comp,fcs).
dept_subj(comp,dld).
dept_subj(comp,dsgt).

subj_teacher(dsa,t1).
subj_teacher(odemc,t2).
subj_teacher(ppl,t3).
subj_teacher(fcs,t4).
subj_teacher(dld,t5).
subj_teacher(dsgt,t6).

dept_div(comp,div1).
dept_div(comp,div2).

div_stu(div1,stu1).
div_stu(div2,stu2).
div_stu(div1,stu3).
div_stu(div2,stu4).

dept_stu(X,Z) :- dept_div(X,Y) , div_stu(Y,Z).


year_subj(X,Z) :- year_dept(X,Y) , dept_subj(Y,Z).
year_stu(X,Z) :- year_dept(X,Y) , dept_stu(Y,Z).
year_teacher(X,Z) :- year_subj(X,Y) , subj_teacher(Y,Z).


coep_dept(X,Z) :- coep_year(X,Y) , year_dept(Y,Z).   
coep_stu(X,Z) :- coep_dept(X,Y) , dept_stu(Y,Z)
coep_teacher(X,Z) :- coep_subj(X,Y) , subj_teacher(Y,Z)





















