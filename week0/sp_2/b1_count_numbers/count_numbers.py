def count_numbers(numbers):
  """Syzdawame set(mnojestvo s nepovtarqshti se elementi)
  ot vsichki chisla ot vida a // b, kydeto a i b sa chisla ot numbers"""
  candidates = set([a // b for a in numbers for b in numbers
                    if a > b and a // b not in numbers])
  while candidates: #dokato v set-a s kandidati ima elemnti
        numbers += candidates #dobavqme kandidatite kym numbers
    #tyrsim novi kandidati
        candidates = set([a // b for a in numbers for b in numbers
                      if a > b and a // b not in numbers])
  #print(numbers)
  return len(numbers)





