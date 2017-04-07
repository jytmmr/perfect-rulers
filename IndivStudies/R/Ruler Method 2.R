
x=date()
L_min = 5
L_max = 25

matches = function(set,goals) {
  new = c()
  pairs = combn(set,2)
  for (j in c(1:ncol(pairs))) {
    new = c(new,abs(pairs[1,j]-pairs[2,j]))
  }
  if (all(is.element(goals,new))) {
    return(1)
  } else {
    return(0)
  }
}

explodingdots = function(sequence,limit) {
  for (i in c(length(sequence):2)) {
    if (sequence[i]==(limit[i]+1)) {
      sequence[i-1] <<- sequence[i-1] + 1
      sequence[i] <<- sequence[i-1] + 1
    }
  }
}

cycle = function(seqence,column) {
  while (sequence[column]<=limit[column]) {
    if (matches(c(sequence,additions),goals)) {
      failed <<- FALSE
      break
    }
    sequence[column] <<- sequence[column] + 1
  }
  explodingdots(sequence,limit)
}



initiatorFunction = function(l){
  print("Made it here", l)
  goals = c(1:l)
  
  q=ceiling(sqrt(.25+2*l)-.5) - 1
  
  additions = c(0,l)
  
  failed <<- TRUE
  
  while (failed) {
    sequence = c(1:q)
    limit = l-c(q:1)
    
    while((sequence[1]==1)&&(failed)) {
      cycle(sequence,q)
    }
    print(paste(as.logical(matches(c(sequence,additions),goals)),"at q =",q))
    
    if (failed) {
      q = q+1
    }
  }
  
  print(sequence)
  
  print(paste("This was for",l))
  print(x)
  print(date())
}


library(doParallel)
registerDoParallel(cores = 10)
foreach(i=L_min:L_max, .packages = "initiatorFunction") %dopar% initiatorFunction(i)

