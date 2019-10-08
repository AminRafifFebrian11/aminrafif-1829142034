def main():

  print("PROGRAM PEMBAGIAN BILANGAN")
  
  a = float (input("MASUKKAN a: "))
  b = float (input("MASUKKAN b: "))
  
  try:
    hasil = a / b
  except ZeroDivisionError:
    print("/nERROR: Nilai b tidak boleh nol")
  else:
    print("/na : ", a)
    print("b : ", b)
    print("a / b = ", hasil)
    
if __name__ == "__main__":
  main()
