#!/usr/bin/env python3
ret = map((lambda f: (lambda x: f(lambda v: x(x)(v))) (lambda x: f(lambda v: x(x)(v)))) 
          (lambda fab: lambda n: 1 if n <= 2 else (fab(n-1) + fab(n-2))), 
          range(10))

print(list(ret))
