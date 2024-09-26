def string_test(S):
  d={"UPPER_CASE":0, "LOWER_CASE":0}
  for c in S:
          if c.isupper():
            d["UPPER_CASE"]+=1
          elif c.islower():
            d["LOWER_CASE"]+=1
          else:
              pass
print ("Original String :",S)
print ("No. of Upper case characters : ", d["UPPER_CASE"]) 
print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test('The quick Brown Fox')

